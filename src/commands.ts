export default [
  //OPEN
  {
    command: "open_file",
    exec: "workbench.action.files.openFileFolder"
  },
  {
    command: "open_folder",
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
  }
];
