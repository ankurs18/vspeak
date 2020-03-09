# CONSTANT = {
#     "number": "$number",
#     "string": "$string",
#     "function": "$function",
#     "selected": "$selected",
# }


class Commands:
    def __init__(self):
        self.commanKeyDict = {
            "open": {
                "tags": ["open"],
                "attributes": {
                    "name": ["file", "folder", "workspace", "terminal", "settings", "new window", ""],
                    "parameter": ["", "", "", "", "", "", ""],
                    "command": [
                        "open_file",
                        "open_file",  # we execute the same command on the vscode side for folder/file, so send the same command from here too
                        "open_workspace",
                        "navigate_terminal",
                        "open_settings",
                        "open_window",
                        "open_file",
                    ],
                    "wordlen": [(2, 3), (2, 3), (2, 3), (2, 3), (2, 3), (3, 4), (1, 1)],
                },
            },
            "run": {
                "tags": ["run"],
                "attributes": {
                    "name": ["file", "project", ""],
                    "parameter": ["", "", ""],
                    "command": [
                        "run_file",
                        "run_project",
                        "run_file",  # could be run_project when nothing is specified, need to understand user's expectation
                    ],
                    "wordlen": [(2, 4), (2, 4), (1, 1)],
                },
            },
            "debug": {
                "tags": ["debug", "debugging", "debugger"],
                "attributes": {
                    "name": ["start", "stop", "project", "pause", "continue", ""],
                    "parameter": ["", "", "", "", "", ""],
                    "command": [
                        "start_debug",
                        "stop_debug",
                        "start_debug",
                        "pause_debug",
                        "continue_debug",
                        "start_debug",
                    ],
                    "wordlen": [(2, 5), (2, 2), (2, 4), (2, 4), (2, 4), (1, 3)],
                },
            },
            "search": {
                "tags": ["search", "find"],
                "attributes": {
                    "name": ["file", "folder", "workspace", "google", ""],
                    "parameter": ["", "", "", "", ""],
                    "command": [
                        "search_workspace",
                        "search_workspace",
                        "search_workspace",
                        "search_google",
                        "search"
                    ],
                    "wordlen": [(2, 4), (2, 4), (2, 3), (2, 2), (1,2)],
                },
            },
            "next": {
                "tags": ["next"],
                "attributes": {
                    "name": ["match", ""],
                    "parameter": ["", ""],
                    "command": ["next_match", "next_match",],
                    "wordlen": [(1, 2), (1, 2)],
                },
            },
            "go": {
                "tags": ["go to", "goto", "navigate to", "move to"],
                "attributes": {
                    "name": ["line", "definition", "class", "file", "terminal"],
                    "parameter": ["number", "", "string", "", ""],
                    "command": [
                        "navigate_line",
                        "navigate_definition",
                        "navigate_class",
                        "navigate_file",
                        "navigate_terminal",
                    ],
                    "wordlen": [(4, 7), (3, 5), (3, 6), (2, 4), (2, 3)],
                },
            },
            "close": {
                "tags": ["close"],
                "attributes": {
                    "name": [
                        "current file",
                        "this file",
                        "all files",
                        "files to the right",
                        "file to the right",
                        "files to the left",
                        "file to the left",
                        "window",
                    ],
                    "parameter": ["", "", "", "", "", ""],
                    "command": [
                        "close_current_file",
                        "close_current_file",
                        "close_all_files",
                        "close_to_the_right",
                        "close_to_the_right",
                        "close_to_the_left",
                        "close_to_the_left",
                        "close_window",
                    ],
                    "wordlen": [
                        (3, 4),
                        (3, 4),
                        (3, 5),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (2, 3),
                    ],
                },
            },
            
            "cut": {
                "tags": ["cut"],
                "attributes": {
                    "name": [""],
                    "parameter": [""],
                    "command": ["cut"],
                    "wordlen": [(1, 1)],
                },
            },
            "copy": {
                "tags": ["copy"],
                "attributes": {
                    "name": [""],
                    "parameter": [""],
                    "command": ["copy"],
                    "wordlen": [(1, 1)],
                },
            },
            "paste": {
                "tags": ["paste"],
                "attributes": {
                    "name": [""],
                    "parameter": [""],
                    "command": ["paste"],
                    "wordlen": [(1, 1)],
                },
            },
            "show": {
                "tags": ["show"],
                "attributes": {
                    "name": ["all commands", "context menu", "next change", "previous change"],
                    "parameter": ["", "", "", ""],
                    "command": ["show_commands", "show_contextMenu", "show_nextChange", "show_previousChange"],
                    "wordlen": [(3, 4), (3, 4), (3, 4), (3, 4)],
                },
            },
            "zoom": {
                "tags": ["zoom"],
                "attributes": {
                    "name": ["in", "out"],
                    "parameter": ["", ""],
                    "command": ["zoom_in", "zoom_out"],
                    "wordlen": [(2, 2), (2, 2)],
                },
            },
            "save": {
                "tags": ["save"],
                "attributes": {
                    "name": ["as", "all", ""],
                    "parameter": ["", "", ""],
                    "command": ["save_as", "save_all", "save"],
                    "wordlen": [(2, 2), (2, 3), (1,2)],
                },
            },
            "scroll": {
                "tags": ["scroll"],
                "attributes": {
                    "name": ["up", "down"],
                    "parameter": ["", ""],
                    "command": ["scroll_up", "scroll_down"],
                    "wordlen": [(2, 2), (2, 2)],
                },
            },
            "comment": {
                "tags": ["comment", "uncomment"],
                "attributes": {
                    "name": ["line", "lines", "selection", ""],
                    "parameter": ["", "", "", ""],
                    "command": ["toggle_comment", "toggle_comment", "toggle_comment", "toggle_comment"],
                    "wordlen": [(2, 3), (2, 3), (2, 3), (1, 1)],
                },
            },
            "extensions": {
                "tags": ["install", "update"],
                "attributes": {
                    "name": ["extension", "extensions"],
                    "parameter": ["", ""],
                    "command": ["install_extension", "update_extension"],
                    "wordlen": [(2, 3), (3, 4)],
                },
            },
            "breakpoint": {
                "tags": ["breakpoint", "breakpoints"],
                "attributes": {
                    "name": ["add", "delete all", "remove all", "delete", "remove", "toggle", "disable all","enable all"],
                    "parameter": ["number", "", "", "number", "number", "", "", ""],
                    "command": ["breakpoint_add", "breakpoint_remove_all", "breakpoint_remove_all", "breakpoint_remove","breakpoint_remove", "breakpoint_toggle", "breakpoint_disable_all", "breakpoint_enable_all"],
                    "wordlen": [(3, 7), (3,4), (3,4),  (3, 7),(3, 7), (2, 2), (3,4), (3,4)],
                },
            },
            "format": {
                "tags": ["format"],
                "attributes": {
                    "name": ["selection", "selected", ""],
                    "parameter": ["", "", ""],
                    "command": ["format_selection", "format_selection", "format_document"],
                    "wordlen": [(2, 3), (2, 3), (1, 3)],
                },
            },
            "compare": {
                "tags": ["compare"],
                "attributes": {
                    "name": ["clipboard", "copied", ""],
                    "parameter": ["", "", ""],
                    "command": ["compare_clipboard", "compare_clipboard", "compare_file"],
                    "wordlen": [(2, 4), (2, 4), (1, 3)],
                },
            },
            # general commands created for continue and stop while debugging but may be used as other context-aware commands;
            # make sure to keep this below the original command as it should have lower priority as 
            # previous exact command may match completely
            "conitnue": {
                "tags": ["continue"],
                "attributes": {
                    "name": [""],
                    "parameter": [""],
                    "command": ["continue"],
                    "wordlen": [(1, 2)],
                },
            },
            "stop": {
                "tags": ["stop"],
                "attributes": {
                    "name": [""],
                    "parameter": [""],
                    "command": ["stop"],
                    "wordlen": [(1, 2)],
                },
            },
        }
        self.transcript = ""
        self.transcriptLength = 0

    def getParams(self, param, argName):
        if param == "number":
            numbers = [int(s) for s in self.transcript if s.isdigit()]
            if len(numbers) == 1:
                return numbers[0]
            else:
                return None

        elif param == "string":
            argIndex = self.transcript.index(argName)
            if argIndex < (len(self.transcript) - 1):
                nextword = self.transcript[argIndex + 1]
                return nextword
            else:
                return None
        return param

    def getCommand(self, transcript):

        self.transcript = transcript.lower().split()
        self.transcriptLength = len(self.transcript)
        attributes = self.getCommandKeyAttributes()
        response = "fallback"
        command = transcript
        paramValue = ""
        if attributes is not None:
            idx = -1
            names = attributes.get("name")
            for i in range(len(names)):
                index = (
                    self.subfinder(self.transcript, names[i].split())
                    if len(names[i]) > 0
                    else 0
                )
                if index > -1:
                    idx = i
                    break
            if idx > -1:
                (minLen, maxLen) = attributes["wordlen"][idx]
                if minLen <= len(self.transcript) <= maxLen:
                    paramValue = self.getParams(
                        attributes.get("parameter")[idx], attributes.get("name")[idx]
                    )
                    response = "success"
                    command = attributes.get("command")[idx]
                    if paramValue is None:
                        response = "fallback"
                        command = transcript

        print(response, command, paramValue, flush=True)
        return
        # return {"response": response, "command": command, "parameter": paramValue}

    def getCommandKeyAttributes(self):
        commandKeys = self.commanKeyDict.keys()
        for key in commandKeys:
            tags = self.commanKeyDict[key].get("tags")
            for tag in tags:
                index = self.subfinder(self.transcript, tag.split())
                if index > -1:
                    return self.commanKeyDict[key].get("attributes")

        return None

    def subfinder(self, mylist, pattern):
        for i in range(len(mylist)):
            if mylist[i] == pattern[0] and mylist[i : i + len(pattern)] == pattern:
                return i
        return -1


def main():
    commandObj = Commands()
    commandObj.getCommand("stop")


if __name__ == "__main__":
    main()
