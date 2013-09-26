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
                "warning_type": matchDict.get("type"),
                "error_number": matchDict.get("errno"),
                "warning_hint": matchDict.get("hint"),
            }

            if matchDict.get("warning_message"):
                warningEntry["warning_message"] = matchDict.get(
                    "warning_message")

            warningsDict[matchDict["file"]].append(warningEntry)

    return warningsDict
