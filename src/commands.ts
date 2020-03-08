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
];
