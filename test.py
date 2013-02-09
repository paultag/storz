#!/usr/bin/env python

from storz.deb import generate_sut_from_debfile
import sys

print generate_sut_from_debfile(sys.argv[1])
