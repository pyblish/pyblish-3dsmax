"""This setup script packages pyblish-3dsmax."""

# Import built-in modules
import importlib
import os

# Import third-party modules
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = os.path.abspath("pyblish_3dsmax/version.py")
version_mod = importlib.import_module("pyblish_3dsmax.version")
version = version_mod.version

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="pyblish-3dsmax",
    version=version,
    packages=find_packages(),
    url="https://github.com/pyblish/pyblish-3dsmax",
    license="LGPL",
    author="Abstract Factory and Contributors",
    author_email="marcus@abstractfactory.io",
    description="Pyblish for 3ds Max.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=classifiers,
    install_requires=[
        "qt.py>=1.3",
        "pyblish_base>=1.2.1",
        "pyblish_lite>=0.8.0",
    ]
)
