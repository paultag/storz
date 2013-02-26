from storz.decompress import digest_firehose_tree
from storz.core import db


def store(r, when):
    obj = digest_firehose_tree(r)
    db.results.insert({
        "result": obj,
        "when": when
    }, safe=True)
