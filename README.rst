PyErf
=====

|travis| |pypi| |wheels| |pythonversion| |docs|

A pure-Python implementation of the error function and inverse error function.

This is a useful package for when you need to calculate some error fuctions
but you don't want to install all of the scipy/numpy stuff.

Usage
-----
You can import the module::

  from pyerf import pyerf
  pyerf.erfinv(0.5)         # 0.476936...
  pyerf.erf(0.5)            # 0.5204998...
  pyerf.erfc(0.5)           # 0.4795001...

or the package::

  import pyerf
  pyerf.erfinv(0.5)         # 0.476936...
  pyerf.erf(0.5)            # 0.5204998...
  pyerf.erfc(0.5)           # 0.4795001...


or only a specific function::

  from pyerf import erfinv as inverse_error_function
  inverse_error_function(0.5)       # 0.476936...

and lastly, you can even use ``import *`` (but that's no longer considered
very Pythonic as it pollutes the namespace)::

  from pyerf import *
  pyerf.erfinv(0.5)         # 0.476936...
  pyerf.erf(0.5)            # 0.5204998...
  pyerf.erfc(0.5)           # 0.4795001...


Changelog
---------
See `CHANGELOG.md`_.


.. |travis| image:: https://img.shields.io/travis/dougthor42/pyerf.svg
  :target: https://travis-ci.org/dougthor42/PyErf
  :alt: Travis-CI (Linux, Max)

.. |pypi| image:: https://img.shields.io/pypi/v/pyerf.svg
  :target: https://pypi.python.org/pypi/pyerf/
  :alt: Latest PyPI version

.. |wheels| image:: https://img.shields.io/pypi/wheel/pyerf.svg
  :target: https://pypi.python.org/pypi/pyerf/
  :alt: Python Wheels

.. |pythonversion| image:: https://img.shields.io/pypi/pyversions/pyerf.svg
  :target: https://pypi.python.org/pypi/pyerf/
  :alt: Supported Python Versions

.. |docs| image:: https://img.shields.io/badge/docs-pythonhosted-brightgreen.svg
  :target: https://pythonhosted.org/pyerf
  :alt: Documentation Status

.. _`CHANGELOG.md`: https://github.com/dougthor42/PyErf/blob/master/CHANGELOG.md
