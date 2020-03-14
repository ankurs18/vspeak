export default [
  //OPEN
  {
    command: "open_file",
    exec: "workbench.action.files.openFileFolder"
  },
  {
    command: "open_workspace",
    exec: "workbench.action.openWorkspace"
  },
  {
    command: "navigate_definition",
    exec: "editor.action.revealDefinition"
  },
  {
    command: "navigate_file",
    exec: "workbench.action.quickOpen"
  },
  {
    command: "format_document",
    exec: "editor.action.formatDocument"
  },
  {
    command: "format_selection",
    exec: "editor.action.formatSelection"
  },
  {
    command: "navigate_terminal",
    exec: "workbench.action.terminal.focus"
  },
  {
    command: "navigate_editor",
    exec: "workbench.action.focusActiveEditorGroup"
  },
  {
    command: "open_terminal",
    exec: "workbench.action.terminal.new"
  },
  {
    command: "close_current_file",
    exec: "workbench.action.closeActiveEditor"
  },
  {
    command: "close_all_files",
    exec: "workbench.action.closeAllEditors"
  },
  {
    command: "close_to_the_right",
    exec: "workbench.action.closeEditorsToTheRight"
  },
  {
    command: "close_to_the_left",
    exec: "workbench.action.closeEditorsToTheLeft"
  },
  {
    command: "close_window",
    exec: "workbench.action.closeWindow"
  },
  {
    command: "next_match",
    exec: "editor.action.nextMatchFindAction"
  },
  {
    command: "search_workspace",
    exec: "filesExplorer.findInWorkspace"
  },
  {
    command: "run_project",
    exec: "workbench.action.debug.run"
  },
  {
    command: "run_file",
    exec: "code-runner.run"
  },
  {
    command: "start_debug",
    exec: "workbench.action.debug.start"
  },
  {
    command: "pause_debug",
    exec: "workbench.action.debug.pause"
  },
  {
    command: "continue_debug",
    exec: "workbench.action.debug.continue"
  },
  {
    command: "stop_debug",
    exec: "workbench.action.debug.stop"
  },
  {
    command: "step_over",
    exec: "workbench.action.debug.stepOver"
  },
  {
    command: "step_into",
    exec: "workbench.action.debug.stepInto"
  },
  {
    command: "step_out",
    exec: "workbench.action.debug.stepOut"
  },
  {
    command: "cut",
    exec: "editor.action.clipboardCutAction"
  },
  {
    command: "copy",
    exec: "editor.action.clipboardCopyAction"
  },
  {
    command: "paste",
    exec: "editor.action.clipboardPasteAction"
  },
  {
    command: "show_commands",
    exec: "workbench.action.showCommands"
  },
  {
    command: "show_contextMenu",
    exec: "editor.action.showContextMenu"
  },
  {
    command: "show_hover",
    exec: "editor.action.showHover"
  },
  {
    command: "show_nextChange",
    exec: "editor.action.dirtydiff.next"
  },
  {
    command: "show_previousChange",
    exec: "editor.action.dirtydiff.previous"
  },
  {
    command: "zoom_in",
    exec: "workbench.action.zoomIn"
  },
  {
    command: "zoom_out",
    exec: "workbench.action.zoomOut"
  },
  {
    command: "save",
    exec: "workbench.action.files.save"
  },
  {
    command: "save_as",
    exec: "workbench.action.files.saveAs"
  },
  {
    command: "save_all",
    exec: "workbench.action.files.saveAll"
  },
  {
    command: "scroll_up",
    exec: "scrollPageUp"
  },
  {
    command: "scroll_down",
    exec: "scrollPageDown"
  },
  {
    command: "open_settings",
    exec: "workbench.action.openSettings"
  },
  {
    command: "add_comment",
    exec: "editor.action.addCommentLine"
  },
  {
    command: "remove_comment",
    exec: "editor.action.removeCommentLine"
  },
  {
    command: "toggle_comment",
    exec: "editor.action.commentLine"
  },
  {
    command: "search",
    exec: "actions.find"
  },
  {
    command: "open_window",
    exec: "workbench.action.newWindow"
  },
  {
    command: "install_extension",
    exec: "workbench.extensions.action.installExtensions"
  },
  {
    command: "update_extension",
    exec: "workbench.extensions.action.updateAllExtensions"
  },
  {
    command: "compare_file",
    exec: "workbench.files.action.compareFileWith"
  },
  {
    command: "compare_clipboard",
    exec: "workbench.files.action.compareWithClipboard"
  },
  {
    command: "breakpoint_toggle",
    exec: "editor.debug.action.toggleBreakpoint"
  },
  {
    command: "breakpoint_remove_all",
    exec: "workbench.debug.viewlet.action.removeAllBreakpoints"
  },
  {
    command: "breakpoint_enable_all",
    exec: "workbench.debug.viewlet.action.enableAllBreakpoints"
  },
  {
    command: "breakpoint_disable_all",
    exec: "workbench.debug.viewlet.action.disableAllBreakpoints"
  },
  {
    command: "new_file",
    exec: "workbench.action.files.newUntitledFile"
  },
  {
    command: "select_icon_theme",
    exec: "workbench.action.selectIconTheme"
  },
  {
    command: "select_theme",
    exec: "workbench.action.selectTheme"
  },
  //GIT
  {
    command: "git_init",
    exec: "git.init"
  },
  {
    command: "git_clone",
    exec: "git.clone"
  },
  {
    command: "git_branch",
    exec: "git.branch"
  },
  {
    command: "git_branch_rename",
    exec: "git.renameBranch"
  },
  {
    command: "git_branch_delete",
    exec: "git.deleteBranch"
  },
  {
    command: "git_push",
    exec: "git.push"
  },
  {
    command: "git_pull",
    exec: "git.pull"
  },
  {
    command: "git_stage",
    exec: "git.stage"
  },
  {
    command: "git_stage_change",
    exec: "git.stageChange"
  },
  {
    command: "git_stage_all",
    exec: "git.stageAll"
  },
  {
    command: "git_stage_all_tracked",
    exec: "git.stageAllTracked"
  },
  {
    command: "git_stage_all_untracked",
    exec: "git.stageAllUntracked"
  },
  {
    command: "git_commit",
    exec: "git.commit"
  },
  {
    command: "git_reset",
    exec: "git.unstage"
  },
  {
    command: "git_reset_all",
    exec: "git.unstageAll"
  },
  {
    command: "git_diff",
    exec: "git.timeline.openDiff"
  }
];
