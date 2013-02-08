#!/usr/bin/env python

from storz.deb import generate_sut_from_deb
import sys

print generate_sut_from_deb(sys.argv[1])
