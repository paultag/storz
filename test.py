#!/usr/bin/env python

from storz.deb import generate_sut_from_deb
import sys

generate_sut_from_deb(sys.argv[1])
