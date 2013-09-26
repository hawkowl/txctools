import re
import json


# Regex from https://gist.github.com/andialbrecht/917126
P_PYLINT_ERROR = re.compile(r"""
^(?P<file>.+?):(?P<line>[0-9]+):\ # file name and line number
\[(?P<type>[a-z])(?P<errno>\d+) # message type and error number, e.g. E0101
(,\ (?P<hint>.+))?\]\ # optional class or function name
(?P<msg>.*) # finally, the error message
""", re.IGNORECASE|re.VERBOSE)



class Jsoniser:

    def __init__(self, warnings):

        self.warnings = warnings


    def parse(self):

        warningsDict = {}

        for line in self.warnings:

            match = re.search(P_PYLINT_ERROR, line)

            if match:
                matchDict = match.groupdict()

                if not warningsDict.get(matchDict["file"]):
                    warningsDict[matchDict["file"]] = []

                warningEntry = {
                    "line": matchDict.get("file"),
                    "warning_type": matchDict.get("type"),
                    "error_number": matchDict.get("errno"),
                    "warning_hint": matchDict.get("hint"),
                }

                if matchDict.get("warning_message"):
                    warningEntry["warning_message"] = matchDict.get(
                        "warning_message")

                warningsDict[matchDict["file"]].append(warningEntry)

        return json.dumps(warningsDict)
