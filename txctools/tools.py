"""
Some helpful tools.
"""

import re

# Regex from https://gist.github.com/andialbrecht/917126
P_PYLINT_ERROR = re.compile(r"^(?P<file>.+?):(?P<line>[0-9]+):\ \[(?P<type>"
    "[a-z])(?P<errno>\d+) (,\ (?P<hint>.+))?\]\ (?P<msg>.*)",
    re.IGNORECASE|re.VERBOSE)


def parsePyLintWarnings(warnings):
    """
    Turns pyLint/TwistedChecker output into something more useful.

    @param warnings: The warnings to process. Needs to be in pyLint's
        'parseable' format.

    @return: L{dict} of L{list}s
    """

    warningsDict = {}

    for line in warnings:

        match = re.search(P_PYLINT_ERROR, line)

        if match:
            matchDict = match.groupdict()

            if not warningsDict.get(matchDict["file"]):
                warningsDict[matchDict["file"]] = []

            warningEntry = {
                "line": matchDict.get("file"),
                "warning_id": matchDict.get("type") + matchDict.get("errno"),
            }

            if matchDict.get("msg"):
                warningEntry["warning_message"] = matchDict.get("msg")

            warningsDict[matchDict["file"]].append(warningEntry)

    return warningsDict



def cleanupMessage(warning, winfo):

    cleanupItems = {
        "C0301": "Line too long",
        "C0103": "Invalid function/variable name",
        "C0302": "Too many lines in module",
        "W9202": "Missing epytext @param",
        "W9012": "Expected 2 blank lines",
        "W9013": "Expected 2 blank lines",
        "W9015": "Too many blank lines",
        "W0311": "Bad indentation"
    }

    if warning in cleanupItems:
        return cleanupItems[warning]
    else:
        return winfo["message"]
