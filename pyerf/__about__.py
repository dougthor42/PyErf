# -*- coding: utf-8 -*-

import os

__all__ = [
    "__author__",
    "__email__",
    "__license__",
    "__version__",
    "__released__",
    "__created__",
    "__project_name__",
    "__project_url__",
    "__package_name__",
    "__description__",
    "__long_descr__",
]


__author__ = "Douglas Thor"
__email__ = "doug.thor@gmail.com"

__license__ = "GNU General Public License v3 (GPLv3)"
__version__ = "0.1.5"
__released__ = "2017-02-27"
__created__ = "2017-02-22"

__project_name__ = "PyErf"
__project_url__ = "https://www.github.com/dougthor42/pyerf"
__package_name__ = "pyerf"

__description__ = "A pure-Python implementation of the error function and inverse error function."
__long_descr__ = __doc__

# Try to read the README file and use that as our long description.
try:
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, os.pardir, "README.rst")) as f:
        __long_descr__ = f.read()
except Exception:
    pass
