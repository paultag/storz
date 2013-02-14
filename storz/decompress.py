# Copyright (c) Paul R. Tagliamonte <paultag@debian.org>, 2013 under the terms
# and conditions of the LGPLv2.1+
# -*- coding: utf-8 -*-


def digest_firehose_tree(root_node):
    ret = {}
    if isinstance(root_node, list):
        return [digest_firehose_tree(x) for x in root_node]
    try:
        for attr in root_node.__slots__:
            ret[attr] = digest_firehose_tree(getattr(root_node, attr))
    except AttributeError:
        return root_node
    return ret
