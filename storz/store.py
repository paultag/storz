from storz.decompress import digest_firehose_tree
from storz.core import db


def store(r):
    obj = digest_firehose_tree(r)
    db.results.insert(obj, safe=True)
