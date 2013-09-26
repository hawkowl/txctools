"""
Generates a report of hotspot problem areas, according to the most warnings.
"""

from __future__ import division
from txctools import tools
import math


class HotspotReport:
    """
    Hotspot report generator.

    @ivar warnings: See L{__init__}

    @ivar fileCounts: L{dict} of L{dict}s that contains information about the
        warnings in a file.

    @ivar warningCounts: L{dict} of L{dict}s that contains information about
        warnings in the project.
    """

    def __init__(self, warnings):
        """
        Set up the Hotspot Report, and process the warnings, if need be.

        @param warnings: Either a L{dict} from {tools.parsePyLintWarnings} or a
            L{list} of pyLint parseable output.
        """
        if isinstance(warnings, dict):
            self.warnings = warnings
        else:
            self.warnings = tools.parsePyLintWarnings(warnings)

        self.fileCounts = {}
        self.warningCounts = {}


    def process(self):
        """
        Process the warnings.
        """
        for filename, warnings in self.warnings.iteritems():

            self.fileCounts[filename] = {}
            fc = self.fileCounts[filename]

            fc["warning_count"] = len(warnings)
            fc["warning_breakdown"] = self._warnCount(warnings)
            self.warningCounts = self._warnCount(warnings,
                warningCount=self.warningCounts)


    def deliverRawResults(self):
        """
        Deliver the results in their raw form.

        @return: L{tuple} of L{fileCounts} and L{warningCounts}.
        """
        return (self.fileCounts, self.warningCounts)


    def deliverTextResults(self):

        output = "=======================\ntxctools Hotspot Report\n"\
        "=======================\n\n"

        fileResults = sorted(self.fileCounts.items(),
            key=lambda x: x[1]["warning_count"], reverse=True)

        output += "Warnings per File\n=================\n"
        count = 0

        for item in fileResults:
            count += 1
            output += "#%s - %s - %s\n" % (count, item[0],
                item[1]["warning_count"])

        output += "\nWarnings Breakdown\n==================\n"
        count = 0
        warningCount = 0

        warningResults = sorted(self.warningCounts.items(),
            key=lambda x: x[1]["count"], reverse=True)

        for item in warningResults:
            warningCount += item[1]["count"]

        for warning, winfo in warningResults:
            count += 1
            output += "#%s - %s - %s (%s%%) - %s\n" % (count, warning,
                winfo["count"], int(winfo["count"] / warningCount * 100),
                tools.cleanupMessage(warning, winfo))

        return output


    def _warnCount(self, warnings, warningCount=None):

        if not warningCount:
            warningCount = {}

        for warning in warnings:
            wID = warning["warning_id"]
            if not warningCount.get(wID):
                warningCount[wID] = {}
                warningCount[wID]["count"] = 1
                warningCount[wID]["message"] = warning.get("warning_message")
            else:
                warningCount[wID]["count"] += 1

        return warningCount
