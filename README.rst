PyErf
=====
A Pure-Python Error Function and Inverse Error Function Package
---------------------------------------------------------------

|travis| |pypi| |wheels| |pythonversion| |docs|

``pyerf`` is a pure-Python implementation of the error function and
inverse error function using the same functions that SciPy_ uses (namely
parts of the Cephes math library, `cprob/ndtr.c`_ and `cprob/ndtri.c`_).

This is a useful package for when you need to calculate some error fuctions
but you don't want to install all of the SciPy_/NumPy_ stuff.


Usage
-----
You can import the module:

.. code-block:: python

  from pyerf import pyerf
  pyerf.erfinv(0.5)         # 0.476936...
  pyerf.erf(0.5)            # 0.5204998...
  pyerf.erfc(0.5)           # 0.4795001...

or the package:

.. code-block:: python

  import pyerf
  pyerf.erfinv(0.5)         # 0.476936...
  pyerf.erf(0.5)            # 0.5204998...
  pyerf.erfc(0.5)           # 0.4795001...

or only a specific function:

.. code-block:: python

  from pyerf import erfinv as inverse_error_function
  inverse_error_function(0.5)       # 0.476936...

and lastly, you can even use ``import *`` (but that's no longer considered
very Pythonic as it pollutes the namespace):

.. code-block:: python

  from pyerf import *
  pyerf.erfinv(0.5)         # 0.476936...
  pyerf.erf(0.5)            # 0.5204998...
  pyerf.erfc(0.5)           # 0.4795001...


Changelog
---------
See `CHANGELOG.md`_.


.. Images and Links

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
.. _`cprob/ndtr.c`: https://github.com/jeremybarnes/cephes/blob/master/cprob/ndtr.c
.. _`cprob/ndtri.c`: https://github.com/jeremybarnes/cephes/blob/master/cprob/ndtri.c
.. _SciPy: https://www.scipy.org/
.. _NumPy: http://www.numpy.org/
