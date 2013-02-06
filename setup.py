#!/usr/bin/env python

from monomoy import __appname__, __version__
from setuptools import setup

long_description = open('README.md', 'r').read()

setup(
    name=__appname__,
    version=__version__,
    packages=[
        'storz'
    ],
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    description='interfaces with firehose',
    license="Expat",
    url="",
    platforms=['any']
)
