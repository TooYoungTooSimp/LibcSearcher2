from collections import *
from functools import *
from glob import glob
from os import path


class LibcSearcher2:
    def __init__(self, db_path):
        self.lookup = defaultdict(set)
        self.db = defaultdict(dict)
        for symbol_file in glob(path.join(db_path, "*.symbols")):
            libc_id = path.splitext(path.basename(symbol_file))[0]
            with open(symbol_file) as f:
                for line in f.read().splitlines():
                    symbol, addr = line.split(' ')
                    self.lookup[(symbol, int(addr, 16))].add(libc_id)
                    self.lookup[(symbol, int(addr[-3:], 16))].add(libc_id)
                    self.db[libc_id][symbol] = int(addr, 16)

    def search(self, cond):
        result = list(filter(len, [self.lookup[c] for c in cond]))
        return list(reduce(lambda x, y: x.intersection(y), result)) if result is not None and len(result) else None

    def dump(self, libc_id, func):
        return self.db[libc_id][func]
