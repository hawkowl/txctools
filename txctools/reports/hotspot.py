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

	def deliverResults(self):

		return (self.fileCounts, self.warningCounts)

	def _warnCount(self, warnings):

		pass