# Copyright (c) Paul R. Tagliamonte <paultag@debian.org>, 2013 under the terms
# and conditions of the GPL-2+.
# -*- coding: utf-8 -*-

from firehose.report import Analysis, Generator, Metadata
from storz.deb import generate_sut_from_debfile


def generate_analysis(gen_name, gen_version, debfilepath):
    """
    Generate an Analysis object for the SUT given via ``debfilepath``,
    and from static checker ``gen_name``, at version ``gen_version``.
    """
    obj = Analysis(
        metadata=Metadata(
            generator=Generator(name=gen_name, version=gen_version),
            sut=generate_sut_from_debfile(debfilepath),
            file_=None,
            stats=None),
        results=[])
    return obj
