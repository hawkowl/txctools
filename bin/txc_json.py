#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd()))

from txctools import Jsoniser

j = Jsoniser(sys.stdin)
print j.parse()