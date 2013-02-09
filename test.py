#!/usr/bin/env python

from storz.deb import generate_sut_from_dsc
import sys

print generate_sut_from_dsc(sys.argv[1])
