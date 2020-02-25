import { spawn } from 'child_process';
import { join } from 'path';

// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "extension" is now active!');

	// Blank command used to activate the extension through the command palette
	let disposable = vscode.commands.registerCommand('extension.activateSpeak', () => {
	});	

	context.subscriptions.push(disposable);
	//context.subscriptions.push(debugDisposable);
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
		console.debug('In run method');
		this.child = this.execFile('python', [join(__dirname, 'tts.py')]).on('error', (error: any) => print(error));
		this.child.stdout.on('data',
			(data: Buffer) => {

				//print(data);
				let commandRunner = new CommandRunner();
				commandRunner.runCommand(data.toString());
			});

		this.child.stderr.on('data', (data: any) => print(data));
	}
}


class CommandRunner {
	runCommand(command: string) {
		print(command);
		let activeTextEditor;
		let commandWords = command.split(' ');
		switch (commandWords[0]) {
			case 'navigate_line':
				let lineNumber = parseInt(commandWords[1]);
				activeTextEditor = vscode.window.activeTextEditor;
				if (activeTextEditor) {
					const range = activeTextEditor.document.lineAt(lineNumber - 1).range;
					activeTextEditor.selection = new vscode.Selection(range.start, range.start);
					activeTextEditor.revealRange(range);
				}
				break;
			case 'copy':
				activeTextEditor = vscode.window.activeTextEditor;
				if (activeTextEditor) {
					const text = activeTextEditor.document.getText(activeTextEditor.selection);
					vscode.env.clipboard.writeText(text);
				}
				break;
			case 'navigate_class':
				let className = commandWords[1];
				// TODO: implement functionality
				break;
			case 'run_file':
				if (activeTextEditor) {
					// TODO: implement functionality
					//activeTextEditor.document.save;
				}
			case 'fallback':
				break;

		}
	}
}

// helper method for printing to console
function print(data: any) {
	console.log('Vspeak Debug: ' + data.toString());
}

// this method is called when your extension is deactivated
export function deactivate() { }
