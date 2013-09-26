txctools
========

Some tools for getting more use out of TwistedChecker.

Dependencies
------------

txctools works with TwistedChecker, so it requires it.

Running
-------

To use txctools, just pipe them the output of TwistedChecker or pyLint as such::

    pylint twisted/ -f parseable | txc_hotspot
