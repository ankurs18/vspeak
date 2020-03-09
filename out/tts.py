from __future__ import division

import re
import sys
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.oauth2 import service_account
import json
import pyaudio
from six.moves import queue
from commands import Commands

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
commandObj = Commands()


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True
        self.commands = {}

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


def listen_print_loop(responses):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        if result.is_final:
            processTranscript2(transcript)


def processTranscript(transcript):
    sys.stdout.flush()
    transcriptWords = transcript.split()
    transcriptWordsCount = len(transcriptWords)
    if "go" in transcriptWords:
        if transcriptWordsCount > 1:
            if "line" in transcriptWords:
                # case: commands may be: go to line x, go to line number x, go
                numbers = [int(s) for s in transcript.split() if s.isdigit()]
                if len(numbers) == 1:
                    print("success", "navigate_line", numbers[0])
                else:
                    # case: if the transcript contains two different numbers, it may be noise or the user error
                    # or it does not have any number; we can't execute navigate_line command in either case
                    print("fallback", transcript)
            elif "definition" in transcriptWords:
                if transcriptWordsCount < 5:
                    excludedWords = set(transcriptWords) - {
                        "go",
                        "to",
                        "definition",
                        "class",
                        "function",
                        "variable",
                        "symbol",
                    }
                    if len(excludedWords) > 0:
                        # commands: go (to) (class/function/variable/symbol) definition
                        print("success", "navigate_definition")
                    else:
                        # case: likely noise or false positive
                        print("fallback", transcript)
                else:
                    # case: likely noise or false positive
                    print("fallback", transcript)
            elif "class" in transcriptWords:
                if transcriptWordsCount > 2:
                    # command: 'go (to) file fileName' (assuming implicitly that the last word will be the fileName)
                    print(
                        "success",
                        "navigate_class",
                        transcriptWords[transcriptWordsCount - 1],
                    )
                else:
                    print("fallback", transcript)
            elif "terminal" in transcriptWords and transcriptWordsCount < 4:
                print("navigate_terminal")
            elif "file" in transcriptWords:
                if transcriptWordsCount > 2:
                    # command: 'go (to) file fileName' (assuming implicitly that the last word will be the fileName)
                    print(
                        "success",
                        "navigate_file",
                        transcriptWords[transcriptWordsCount - 1],
                    )
                else:
                    print("fallback", transcript)
            else:
                print("fallback")
        else:
            # case: 'go' by itself has no meaning, we need another argument to gather where do we need to navigate
            print("fallback", transcript)
    elif "copy" in transcript:
        if transcriptWordsCount == 1:
            # commands: copy
            print("success", "copy")
        elif "file" in transcriptWords < 4 and (
            len(set(transcriptWords) - {"copy", "current", "this"})
        ):
            # case: commands: copy (current/this) file
            print("success", "copy_file")
        else:
            # case: the user may want to copy something else which we don't support yet or the detected 'copy' phrase may be noise
            print("fallback", transcript)
    elif "format" in transcriptWords:
        if transcriptWordsCount == 1:
            # commands: format
            print("success", "format_document")
        else:
            if "selection" in transcriptWords or "selected" in transcriptWords:
                # commands: format selected text, format selected, format selection
                print("success", "format_selection")
            elif transcriptWordsCount == 2 and (
                "text" in transcriptWords or "document" in transcriptWords
            ):
                # commands: format text or format document
                print("success", "format_document")
            else:
                # case: detected 'format' should be false positive
                print("fallback", transcript)
    elif (
        "terminal" in transcriptWords
        and "open" in transcriptWords
        and transcriptWordsCount < 5
    ):
        # commands: open (a) (new) terminal
        print("success", "open_terminal")

    elif "run" in transcriptWords:
        if transcriptWordsCount == 1:
            # case: user may want to run the entire project, my interpretation is running this file (need to evaluate this)
            print("run_file")
        # case: discarded cases of noise or false positives
        elif (
            transcriptWordsCount < 4
            and len(set(transcriptWords) - {"this", "current", "file", "project"}) > 0
        ):
            # case: discarded cases of noise or false positives
            if "file" in transcriptWords:
                print("run_file")
            elif "project" in transcriptWords:
                print("run_project")
            else:
                print("fallback", transcript)
        else:
            print("fallback", transcript)

    else:
        # default case when neither a command is matched nor a fallback is reached
        # but we still output the transcript for debugging and analysing
        print("fallback", transcript)


def processTranscript2(transcript):
    commandObj.getCommand(transcript)


def main():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = "en-IN"  # a BCP-47 language tag
    dialogflow_key = json.load(open(sys.path[0] + "/chatbot.json"))
    credentials = service_account.Credentials.from_service_account_info(dialogflow_key)
    client = speech.SpeechClient(credentials=credentials)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )
    streaming_config = types.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (
            types.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        try:
            listen_print_loop(responses)
        except:
            main()


if __name__ == "__main__":
    main()
