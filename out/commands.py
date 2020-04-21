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
                    "name": [
                        "new file",
                        "file",
                        "folder",
                        "workspace",
                        "terminal",
                        "settings",
                        "new window",
                        "",
                    ],
                    "parameter": ["", "", "", "", "", "", "", ""],
                    "command": [
                        "new_file",
                        "open_file",
                        "open_file",  # we execute the same command on the vscode side for folder/file, so send the same command from here too
                        "open_workspace",
                        "navigate_terminal",
                        "open_settings",
                        "open_window",
                        "open_file",
                    ],
                    "wordlen": [
                        (3, 4),
                        (2, 3),
                        (2, 3),
                        (2, 3),
                        (2, 3),
                        (2, 3),
                        (3, 4),
                        (1, 1),
                    ],
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
            "step": {
                "tags": ["step", "stepover"],
                "attributes": {
                    "name": ["over", "into", "out", "stepover"],
                    "parameter": ["", "", ""],
                    "command": ["step_over", "step_into", "step_out", "step_out"],
                    "wordlen": [(2, 3), (2, 3), (2, 3), (1, 2)],
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
                        "search",
                    ],
                    "wordlen": [(2, 4), (2, 4), (2, 3), (2, 2), (1, 2)],
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
                    "name": [
                        "line",
                        "definition",
                        "class",
                        "file",
                        "terminal",
                        "editor",
                    ],
                    "parameter": ["number", "", "string", "", "", ""],
                    "command": [
                        "navigate_line",
                        "navigate_definition",
                        "navigate_class",
                        "navigate_file",
                        "navigate_terminal",
                        "navigate_editor",
                    ],
                    "wordlen": [(4, 7), (3, 5), (3, 6), (2, 5), (2, 5), (2, 5)],
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
                        "editors to the right",
                        "editor to the right",
                        "editors to the left",
                        "editor to the left",
                        "window",
                        "file",
                        "editor",
                        "others",
                        "other"
                    ],
                    "parameter": ["", "", "", "", "", "", "","", "", "", "", "", "","", "", ""],
                    "command": [
                        "close_current_file",
                        "close_current_file",
                        "close_all_files",
                        "close_to_the_right",
                        "close_to_the_right",
                        "close_to_the_left",
                        "close_to_the_left",
                        "close_to_the_right",
                        "close_to_the_right",
                        "close_to_the_left",
                        "close_to_the_left",
                        "close_window",
                        "close_current_file",
                        "close_current_file",
                        "close_other",
                        "close_other"
                    ],
                    "wordlen": [
                        (3, 4),
                        (3, 4),
                        (3, 5),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (3, 6),
                        (2, 3),
                        (2, 2),
                        (2, 2),
                        (2, 4),
                        (2, 4),
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
                    "name": [
                        "all commands",
                        "context menu",
                        "next change",
                        "previous change",
                    ],
                    "parameter": ["", "", "", ""],
                    "command": [
                        "show_commands",
                        "show_contextMenu",
                        "show_nextChange",
                        "show_previousChange",
                    ],
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
                    "wordlen": [(2, 2), (2, 3), (1, 2)],
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
                    "command": [
                        "toggle_comment",
                        "toggle_comment",
                        "toggle_comment",
                        "toggle_comment",
                    ],
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
                    "name": [
                        "add",
                        "delete all",
                        "remove all",
                        "delete",
                        "remove",
                        "toggle",
                        "disable all",
                        "enable all",
                    ],
                    "parameter": ["number", "", "", "number", "number", "", "", ""],
                    "command": [
                        "breakpoint_add",
                        "breakpoint_remove_all",
                        "breakpoint_remove_all",
                        "breakpoint_remove",
                        "breakpoint_remove",
                        "breakpoint_toggle",
                        "breakpoint_disable_all",
                        "breakpoint_enable_all",
                    ],
                    "wordlen": [
                        (3, 7),
                        (3, 4),
                        (3, 4),
                        (3, 7),
                        (3, 7),
                        (2, 2),
                        (3, 4),
                        (3, 4),
                    ],
                },
            },
            "format": {
                "tags": ["format"],
                "attributes": {
                    "name": ["selection", "selected", ""],
                    "parameter": ["", "", ""],
                    "command": [
                        "format_selection",
                        "format_selection",
                        "format_document",
                    ],
                    "wordlen": [(2, 3), (2, 3), (1, 3)],
                },
            },
            "compare": {
                "tags": ["compare"],
                "attributes": {
                    "name": ["clipboard", "copied", ""],
                    "parameter": ["", "", ""],
                    "command": [
                        "compare_clipboard",
                        "compare_clipboard",
                        "compare_file",
                    ],
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
            "theme": {
                "tags": ["icon", "theme"],
                "attributes": {
                    "name": ["icon theme", ""],
                    "parameter": ["", ""],
                    "command": ["select_icon_theme", "select_theme"],
                    "wordlen": [(2, 4), (2, 4)],
                },
            },
            "git": {
                "tags": [
                    "git",
                    "push",
                    "pull",
                    "revert",
                    "commit",
                    "git reset",
                    "git add",
                    "unstage",
                    "branch",
                    "branches",
                    "stage",
                    "clone",
                ],
                "init": {
                    "tags": ["git init", "init", "git new"],
                    "attributes": {
                        "name": [""],
                        "parameter": [""],
                        "command": ["git_init"],
                        "wordlen": [(2, 3)],
                    },
                },
                "clone": {
                    "tags": ["git clone"],
                    "attributes": {
                        "name": [""],
                        "parameter": [""],
                        "command": ["git_clone"],
                        "wordlen": [(2, 3)],
                    },
                },
                "diff": {
                    "tags": ["git diff", "git difference"],
                    "attributes": {
                        "name": ["", ""],
                        "parameter": ["", ""],
                        "command": ["git_diff", "git_diff"],
                        "wordlen": [(2, 3), (2, 3)],
                    },
                },
                "push": {
                    "tags": ["git push", "push"],
                    "attributes": {
                        "name": ["changes", "files", "branch", "change", "file", ""],
                        "parameter": ["", "", "", "", "", ""],
                        "command": [
                            "git_push",
                            "git_push",
                            "git_push",
                            "git_push",
                            "git_push",
                            "git_push",
                        ],
                        "wordlen": [(2, 4), (2, 4), (2, 4), (2, 4), (2, 4), (2, 3)],
                    },
                },
                "status": {
                    "tags": ["git status", "status"],
                    "attributes": {
                        "name": [""],
                        "parameter": [""],
                        "command": ["git_status"],
                        "wordlen": [(2, 3)],
                    },
                },
                "pull": {
                    "tags": ["git pull", "pull"],
                    "attributes": {
                        "name": ["changes", "files", "branch", "change", "file", ""],
                        "parameter": ["", "", "", "", "", ""],
                        "command": [
                            "git_pull",
                            "git_pull",
                            "git_pull",
                            "git_pull",
                            "git_pull",
                            "git_pull",
                        ],
                        "wordlen": [(2, 4), (2, 4), (2, 4), (2, 4), (2, 4), (2, 3)],
                    },
                },
                "reset": {
                    "tags": ["git reset", "reset", "unstage"],
                    "attributes": {
                        "name": [
                            "changes",
                            "files",
                            "change",
                            "file",
                            "all",
                            "everything",
                            "",
                        ],
                        "parameter": ["", "", "", "", "", "", ""],
                        "command": [
                            "git_reset",
                            "git_reset",
                            "git_reset",
                            "git_reset",
                            "git_reset_all",
                            "git_reset_all",
                            "git_reset",
                        ],
                        "wordlen": [
                            (2, 4),
                            (2, 4),
                            (2, 4),
                            (2, 4),
                            (3, 4),
                            (2, 3),
                            (2, 3),
                        ],
                    },
                },
                "add": {
                    "tags": ["git add", "add", "stage"],
                    "attributes": {
                        "name": [
                            "changes",
                            "files",
                            "change",
                            "file",
                            "all",
                            "everything",
                            "tracked",
                            "untracked",
                            "",
                        ],
                        "parameter": ["", "", "", "", "", "", "", "", ""],
                        "command": [
                            "git_stage_change",
                            "git_stage",
                            "git_stage_change",
                            "git_stage_all",
                            "git_stage_all",
                            "git_stage_all_tracked",
                            "git_stage_all_untracked",
                            "git_stage",
                        ],
                        "wordlen": [
                            (2, 4),
                            (2, 4),
                            (2, 4),
                            (2, 4),
                            (3, 4),
                            (3, 5),
                            (3, 5),
                            (2, 3),
                        ],
                    },
                },
                "commit": {
                    "tags": ["git commit", "commit"],
                    "attributes": {
                        "name": ["changes", "files", "change", "file", ""],
                        "parameter": ["", "", "", "", "", ""],
                        "command": [
                            "git_commit",
                            "git_commit",
                            "git_commit",
                            "git_commit",
                            "git_commit",
                            "git_commit",
                        ],
                        "wordlen": [(2, 4), (2, 4), (2, 4), (2, 4), (2, 3)],
                    },
                },
                "branch": {
                    "tags": ["git branch", "branch", "branches"],
                    "attributes": {
                        "name": ["delete", "rename", ""],
                        "parameter": ["", "", ""],
                        "command": [
                            "git_branch_delete",
                            "git_branch_rename",
                            "git_branch",
                        ],
                        "wordlen": [(2, 3), (2, 3), (2, 3)],
                    },
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
        attributes = self.getCommandKeyAttributes(None)
        response = "fallback"
        command = transcript
        paramValue = ""
        # print(attributes)
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

    def getCommandKeyAttributes(self, subcommand):

        commandKeys = (
            list(subcommand.keys())
            if subcommand is not None
            else list(self.commanKeyDict.keys())
        )
        commandObj = subcommand if subcommand is not None else self.commanKeyDict
        l2 = ["tags"]
        commandKeys = [x for x in commandKeys if x not in l2]
        for key in commandKeys:
            tags = commandObj[key].get("tags")
            for tag in tags:
                index = self.subfinder(self.transcript, tag.split())
                if index > -1:
                    # self.transcript = self.transcript[index:]
                    if commandObj[key].get("attributes") is not None:
                        return commandObj[key].get("attributes")
                    else:
                        return self.getCommandKeyAttributes(commandObj[key])

        return None

    def subfinder(self, mylist, pattern):
        for i in range(len(mylist)):
            if mylist[i] == pattern[0] and mylist[i : i + len(pattern)] == pattern:
                return i
        return -1


# def main():
#     commandObj = Commands()
#     commandObj.getCommand("close window")


# if __name__ == "__main__":
#     main()
