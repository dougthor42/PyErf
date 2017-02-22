# -*- coding: utf-8 -*-
"""
setup.py file for PyErf.
"""
#------------------------------------------------------------------------
### Imports
#------------------------------------------------------------------------
# Standard Library
import logging
import os
from setuptools import setup, find_packages
import sys

about = {}
base_dir = os.path.dirname(__file__)
sys.path.insert(0, base_dir)
with open(os.path.join(base_dir, "pyerf", "__about__.py")) as f:
    exec(f.read(), about)

with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

# turn off logging if we're going to build a distribution
logging.disable(logging.CRITICAL)

classifiers = [
    "Development Status :: 1 - Planning",
]

requires = [
]

setup(
    name=about["__package_name__"],
    version=about["__version__"],

    description=about["__description__"],
    long_description=long_description,
    url=about["__project_url__"],

    author=about["__author__"],
    license=about["__license__"],

    packages=find_packages(),
    classifiers=classifiers,

    requires=requires,
)
