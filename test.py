#!/usr/bin/env python

from storz.wrapper import generate_analysis
import sys


obj = generate_analysis('lintian', '1.0', sys.argv[1])
print obj
