import sys
import itertools
import glob

def find_(s, iterable):
    """
    A function that can find a sequence's start in an iterable.
    
    >>> f = find_
    >>> f('a', 'abc')
    0
    >>> f('abc', 'abc')
    0
    >>> f('b', 'abc')
    1
    >>> f('bc', 'abc')
    1
    >>> f('foo', 'bar')
    -1
    >>> f('foo', 'oo')
    -1
    """
    len_s = len(s)
    ok = 0  # symbols ok

    for i, c in enumerate(iterable):
        if s[ok] != c:
            ok = 0
        else:
            ok += 1
            if ok == len_s:
                return (i + 1) - ok

    return -1

def file_symbols(path):
    """
    A generator that yields every single character of a file.
    """
    f = open(path)
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            yield c

def many_files_symbols(paths):
    symbol_generators = (file_symbols(path) for path in paths)
    generators_chain = itertools.chain(*symbol_generators)
    return generators_chain
    
def usage():
    print 'finder.py <string> <wildcard>'

if __name__ == '__main__':
    try:
        s = sys.argv[1]
        wildcard = sys.argv[2]
    except IndexError:
        usage()
    else:
        print find_(s, many_files_symbols(glob.glob(wildcard)))
