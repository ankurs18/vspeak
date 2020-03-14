import { spawn } from "child_process";
import { join } from "path";

// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from "vscode";
import COMMANDS from "./commands";
var MAP = new Map();
// var HashMap = require("hashmap");
// var map: {
//   set: (arg0: any, arg1: any) => void;
//   has: (arg0: string) => any;
//   get: (arg0: string) => string;
// };

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
  console.log('Congratulations, your extension "extension" is now active!');

  // Temporary blank command used to activate the extension through the command palette
  let disposable = vscode.commands.registerCommand(
    "extension.activateSpeak",
    () => {}
  );

  context.subscriptions.push(disposable);
  new SpeechListener(context);

  for (var i = 0; i < COMMANDS.length; i++) {
    var item = COMMANDS[i];
    MAP.set(COMMANDS[i].command, COMMANDS[i].exec);
  }
}

class SpeechListener {
  private execFile: any;
  private child: any;

  constructor(context: vscode.ExtensionContext) {
    this.execFile = spawn;
    this.run();
  }

  run() {
    print("Trying to run speech detection");
    this.child = this.execFile("python3", [
      join(__dirname, "tts.py")
    ]).on("error", (error: any) => print(error));
    this.child.stdout.on("data", (data: Buffer) => {
      //print(data);
      let commandRunner = new CommandRunner();
      commandRunner.runCommand(data.toString().trim());
    });

    this.child.stderr.on("data", (data: any) => print(data));
  }
}

class CommandRunner {
  runCommand(receivedString: string) {
    print("Command received: " + receivedString);
    let activeTextEditor;
    let lineNumber;
    const words = receivedString.split(" ");
    const status = words[0] === "success";
    // var result = receivedString.substr(receivedString.indexOf(" ") + 1);
    // print(result.trim());

    // added vscode.window.state.focused because commands should only run when vs code window is in the foreground
    if (status && vscode.window.state.focused) {
      const commandWords = words.slice(1);
      if (MAP.has(commandWords[0])) {
        vscode.commands.executeCommand(MAP.get(commandWords[0]));
      } else {
        switch (commandWords[0]) {
          case "continue":
            if (vscode.debug.activeDebugSession) {
              print("Context aware continue while in debug");
              vscode.commands.executeCommand("workbench.action.debug.continue");
            } else {
              print('Falling back as no context found for "continue"');
            }
            break;
          case "stop":
            if (vscode.debug.activeDebugSession) {
              print('Context aware "stop" while in debug');
              vscode.commands.executeCommand("workbench.action.debug.stop");
            } else {
              print('Falling back as no context found for "stop"');
            }
            break;
          case "continue":
            if (vscode.debug.activeDebugSession) {
              vscode.commands.executeCommand("workbench.action.debug.continue");
            }
            break;
          case "search_google":
            activeTextEditor = vscode.window.activeTextEditor;
            if (activeTextEditor) {
              const text = activeTextEditor.document.getText(
                activeTextEditor.selection
              );
              vscode.env.openExternal(
                vscode.Uri.parse("https://www.google.com/search?q=" + text)
              );
            }
            break;
          case "navigate_line":
            lineNumber = parseInt(commandWords[1]);
            activeTextEditor = vscode.window.activeTextEditor;
            if (activeTextEditor) {
              const range = activeTextEditor.document.lineAt(lineNumber - 1)
                .range;
              activeTextEditor.selection = new vscode.Selection(
                range.start,
                range.start
              );
              activeTextEditor.revealRange(range);
            }
            break;
          case "breakpoint_add":
            lineNumber = parseInt(commandWords[1]);
            activeTextEditor = vscode.window.activeTextEditor;
            if (activeTextEditor) {
              let position = new vscode.Position(lineNumber - 1, 0);
              let location = new vscode.Location(
                activeTextEditor.document.uri,
                position
              );
              let breakpointToAdd = [
                new vscode.SourceBreakpoint(location, true)
              ];
              vscode.debug.addBreakpoints(breakpointToAdd);
            }
            break;
          case "breakpoint_remove":
            lineNumber = parseInt(commandWords[1]);
            activeTextEditor = vscode.window.activeTextEditor;
            if (activeTextEditor) {
              let existingBreakPoints = vscode.debug.breakpoints;
              for (let breakpoint of existingBreakPoints) {
                if (
                  breakpoint instanceof vscode.SourceBreakpoint &&
                  breakpoint.location.uri.path ===
                    activeTextEditor.document.uri.path &&
                  breakpoint.location.range.start.line === lineNumber - 1
                ) {
                  vscode.debug.removeBreakpoints([breakpoint]);
                }
              }
            }
            break;
          // case "navigate_definition":
          //   vscode.commands.executeCommand("editor.action.revealDefinition");
          //   break;
          // case "navigate_file":
          //   vscode.commands.executeCommand("workbench.action.quickOpen");
          //   vscode.window.showQuickPick();
          // console.debug(vscode.workspace.);
          // console.debug(vscode.workspace.asRelativePath("."));
          // vscode.workspace.fs
          //   .readDirectory(
          //     vscode.Uri.file(vscode.workspace.asRelativePath("."))
          //   )
          //   .then(files => {
          //     let filenames: string[] = files.map(
          //       (filename, filetype) => filename[0]
          //     );
          //     vscode.window.showQuickPick(filenames);
          //   });
          // break;
          case "copy":
            activeTextEditor = vscode.window.activeTextEditor;
            if (activeTextEditor) {
              const text = activeTextEditor.document.getText(
                activeTextEditor.selection
              );
              vscode.env.clipboard.writeText(text);
            }
            break;
          case "navigate_class":
            let className = commandWords[1];
            // TODO: implement functionality
            break;
          case "run_file":
            activeTextEditor = vscode.window.activeTextEditor;
            if (activeTextEditor) {
              activeTextEditor.document.save(); //should probably save all files
              const currentFileName = activeTextEditor.document.fileName;
              const activeTerminal = vscode.window.activeTerminal;
              if (activeTerminal) {
                if (activeTextEditor.document.languageId === "python") {
                  // TODO: implement functionality for other languages
                  activeTerminal.sendText("python " + currentFileName);
                } else {
                  vscode.window.showErrorMessage(
                    "Oops! Unsupported language for run commapnd"
                  );
                }
              }
            }
            break;
          case "copy_file":
            // TODO: implement functionality
            break;
          case "git_status":
            const activeTerminal = vscode.window.activeTerminal;
            if (
              activeTerminal &&
              vscode.extensions.getExtension("vscode.git")
            ) {
              activeTerminal.sendText("git status");
            }
            break;
        }
      }
    }
  }
}

// helper method for printing to console
function print(data: any) {
  console.log("Vspeak Debug: " + data.toString());
}

// this method is called when your extension is deactivated
export function deactivate() {}
