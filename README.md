# LibcSearcher2
Maybe a faster LibcSearcher

## Requirements

- Python 2 or 3

- [libc-database]: https://github.com/niklasb/libc-database	"You need build your own libc-database."

  

## Install

```sh
pip install LibcSearcher2
```



## Usage

```python
from LibcSearcher2 import LibcSearcher2
# Initialize a LibcSearcher2 instance
searcher = LibcSearcher2(db_path) # db_path: libc-database/db
# Search a symbol with its leaked address
searcher.search_simple(symbol, address)
# Search multiple symbols at once
searcher.search([(sym1, addr1 & 0xfff), (sym2, addr2 & 0xfff), ...])
# Both method will returns a list of libc_id, you need specify one to use later.
# Dump offset of another symbol with a libc_id
searcher.dump(libc_id, symbol)
# Create a functor to dump real address of symbols.
ret = searcher.dumps(libc_id, symbol, address)
# Then you can use it to dump real addresses
ret("read"), ret("write"), ret("str_bin_sh")
```

