"""
Generates a report of hotspot problem areas, according to the most warnings.
"""

from txctools import tools


class HotspotReport:

    def __init__(self, warnings):

        if isinstance(warnings, dict):
            self.warnings = warnings
        else:
            self.warnings = tools.parsePyLintWarnings(warnings)

        self.fileCounts = {}
        self.warningCounts = {}


    def process(self):

        for filename, warnings in self.warnings.iteritems():

            self.fileCounts[filename] = {}
            fc = self.fileCounts[filename]

            fc["warning_count"] = len(warnings)
            fc["warning_breakdown"] = self._warnCount(warnings)
            self.warningCounts = self._warnCount(warnings,
                warningCount=self.warningCounts)


    def deliverRawResults(self):

        return (self.fileCounts, self.warningCounts)


    def deliverTextResults(self):

        output = "=======================\ntxctools HotSpot Report\n"\
        "=======================\n\n"

        fileResults = sorted(self.fileCounts.items(),
            key=lambda x: x[1]["warning_count"], reverse=True)

        output += "Warnings per File\n=================\n"

        count = 0

        for item in fileResults:
            count += 1
            output += "#%s - %s - %s\n" %(count, item[0],
                item[1]["warning_count"])

        return output


    def _warnCount(self, warnings, warningCount=None):

        if not warningCount:
            warningCount = {}

        for warning in warnings:

            if not warningCount.get(warning["warning_id"]):
                warningCount[warning["warning_id"]] = 1
            else:
                warningCount[warning["warning_id"]] += 1

        return warningCount
