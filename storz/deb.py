# Copyright (c) Paul R. Tagliamonte <paultag@debian.org>, 2013 under the terms
# and conditions of the GPL-2+.
# -*- coding: utf-8 -*-

import os.path

from storz.errors import StorsError

from debian.deb822 import Dsc
from debian.debfile import DebFile

from firehose.report import DebianBinary, DebianSource


def parse_version(version):
    """
    Split a Debian version up into local and upstream parts.

    .. Warning::
        Although this should be 100% perfect for Debian package in the
        archive, it is very easy to craft a Debian binary that is native
        *and* has a `-` in the version string. However, seeing as how Debian
        policy section 5.6.12 (Version), prohibits this, we should be OK.
        In particular::
            The upstream_version may contain only alphanumerics and the
            characters . + - : ~ (full stop, plus, hyphen, colon, tilde)
            and should start with a digit. If there is no debian_revision
            then hyphens are not allowed; if there is no epoch then colons
            are not allowed.
    """
    local = None
    if "-" in version:
        version, local = version.rsplit("-", 1)
    return version, local


def generate_sut_from_deb(path):
    """ Generate a Firehose SUT from a .deb file.  """
    obj = DebFile(filename=path, mode='r')
    control = obj.debcontrol()
    version = control['Version']
    version, local = parse_version(version)
    name, arch = [control[x] for x in ['Package', 'Architecture']]
    return DebianBinary(name, version, local, arch)


def generate_sut_from_dsc(path):
    """ Generate a Firehose SUT from a .dsc file. """
    fd = open(path, 'r')
    obj = Dsc(sequence=fd)
    version = obj['Version']
    version, local = parse_version(version)
    source = obj['Source']
    return DebianSource(source, version, local)


class StorzUnknownExtentionError(StorsError):
    pass


class StorzNoSuchFile(StorsError):
    pass


def generate_sut_from_debfile(path):
    """
    Generate a Firehose SUT from a .dsc or .deb file.

    ``path`` will be expanded (for both ~/foo, and
    absolute path).

    If ``path`` does not exist, this method will raise a
    ``StorzNoSuchFile`` error.

    If the extention isn't known, this method will raise a
    ``StorzUnknownExtentionError``.

    Currently supported types:

        * .dsc
        * .deb
    """
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.exists(path):
        raise StorzNoSuchFile(path)

    handlers = {
        ".deb": generate_sut_from_deb,
        ".dsc": generate_sut_from_dsc
    }
    for handler in handlers:
        if path.endswith(handler):
            return handlers[handler](path)
    raise StorzUnknownExtentionError(path)
