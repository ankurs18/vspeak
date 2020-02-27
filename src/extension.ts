import { spawn } from 'child_process';
import { join } from 'path';

// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	console.log('Congratulations, your extension "extension" is now active!');

	// Temporary blank command used to activate the extension through the command palette
	let disposable = vscode.commands.registerCommand('extension.activateSpeak', () => {
	});

	context.subscriptions.push(disposable);
	new SpeechListener(context);
}


class SpeechListener {
	private execFile: any;
	private child: any;


	constructor(context: vscode.ExtensionContext) {
		this.execFile = spawn;
		this.run();
	}

	run() {
		print('Trying to run speech detection');
		this.child = this.execFile('python', [join(__dirname, 'tts.py')]).on('error', (error: any) => print(error));
		this.child.stdout.on('data',
			(data: Buffer) => {

				//print(data);
				let commandRunner = new CommandRunner();
				commandRunner.runCommand(data.toString().trim());
			});

		this.child.stderr.on('data', (data: any) => print(data));
	}
}


class CommandRunner {
	runCommand(receivedString: string) {
		print('Command received: ' + receivedString);
		let activeTextEditor;
		const words = receivedString.split(' ');
		const status = words[0] === 'success';
		if (status) {
			const commandWords = words.slice(1);
			switch (commandWords[0]) {
				case 'navigate_line':
					const lineNumber = parseInt(commandWords[1]);
					activeTextEditor = vscode.window.activeTextEditor;
					if (activeTextEditor) {
						const range = activeTextEditor.document.lineAt(lineNumber - 1).range;
						activeTextEditor.selection = new vscode.Selection(range.start, range.start);
						activeTextEditor.revealRange(range);
					}
					break;
				case 'navigate_definition':
					vscode.commands.executeCommand('editor.action.revealDefinition');
					break;
				case 'copy':
					activeTextEditor = vscode.window.activeTextEditor;
					if (activeTextEditor) {
						const text = activeTextEditor.document.getText(activeTextEditor.selection);
						vscode.env.clipboard.writeText(text);
					}
					break;

				case 'format_document':
					vscode.commands.executeCommand('editor.action.formatDocument');
					break;
				case 'format_selection':
					vscode.commands.executeCommand('editor.action.formatSelection');
					break;
				case 'navigate_terminal':
					vscode.commands.executeCommand('workbench.action.terminal.focus');
					break;
				case 'open_terminal':
					vscode.commands.executeCommand('workbench.action.terminal.new');
					break;
				case 'navigate_class':
					let className = commandWords[1];
					// TODO: implement functionality
					break;
				case 'run_file':
					activeTextEditor = vscode.window.activeTextEditor;
					if (activeTextEditor) {
						activeTextEditor.document.save(); //should probably save all files
						const currentFileName = activeTextEditor.document.fileName;
						const activeTerminal = vscode.window.activeTerminal;
						if (activeTerminal) {
							// TODO: implement functionality for other languages
							activeTerminal.sendText('python ' + currentFileName);
						}
					}

				case 'copy_file':
					// TODO: implement functionality
					break;


			}

		}

	}
}

// helper method for printing to console
function print(data: any) {
	console.log('Vspeak Debug: ' + data.toString());
}

// this method is called when your extension is deactivated
export function deactivate() { }
