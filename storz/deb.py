# Copyright (c) Paul R. Tagliamonte <paultag@debian.org>, 2013 under the terms
# and conditions of the GPL-2+.

from debian.debfile import DebFile


def generate_sut_from_deb(path):
    """ Generate a Firehose SUT from a .deb file.  """
    obj = DebFile(filename=path, mode='r')
    control = obj.debcontrol()
    version = control['Version']
    local = None
    if "-" in version:
        version, local = version.rsplit("-", 1)
    name, arch = [control[x] for x in ['Package', 'Architecture']]

    # XXX: Implement SUT generation with name, version, release, arch
