#!/usr/bin/env python
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.getcwd()))

from txctools import parsePyLintWarnings

print json.dumps(parsePyLintWarnings(sys.stdin))