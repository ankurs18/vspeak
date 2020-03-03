# CONSTANT = {
#     "number": "$number",
#     "string": "$string",
#     "function": "$function",
#     "selected": "$selected",
# }


class Commands:
    def __init__(self, transcript):
        self.commanKeyDict = {
            "go": {
                "maxwords": 5,
                "tags": ["go to", "goto", "naviagte to", "move to"],
                "arguments": {
                    "name": ["line", "definition"],
                    "parameter": ["number", ""],
                    "command": ["navigate_line", "navigate_definition"],
                },
            }
        }
        self.transcript = transcript.lower()

    def getParams(self, param, argName):
        if param == "number":
            numbers = [int(s) for s in self.transcript.split() if s.isdigit()]
            if len(numbers) == 1:
                return numbers[0]
            else:
                return None

        if param == "string":
            nextword = self.transcript[self.transcript.index(argName) + 1]
            if nextword is not None:
                return nextword
            else:
                return None

    def getCommand(self):
        arguments = self.getCommandKey()

        command = "fallback"
        paramValue = ""
        if arguments is not None:
            idx = -1
            for argument in arguments.get("name"):
                index = self.transcript.find(argument)
                if index > -1:
                    idx = index

            if idx > -1:
                paramValue = getParams(
                    arguments.get("parameter")[idx], arguments.get("name")[idx]
                )
                # if paramValue is None:
                #     return {"command": command, "parameter": paramValue}
                command = arguments.command[idx]
        return {"command": command, "parameter": paramValue}

    def getCommandKey(self):
        commandKeys = self.commanKeyDict.keys()
        for key in commandKeys:
            tags = self.commanKeyDict[key].get("tags")
            for tag in tags:
                index = self.transcript.find(tag)
                if index > -1:
                    self.transcript = self.transcript[index:]
                    return self.commanKeyDict[key].get("arguments")
                else:
                    return None


def main():
    commandObj = Commands("goto line 10")
    final = commandObj.getCommand()


if __name__ == "__main__":
    main()
