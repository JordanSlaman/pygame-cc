

def one(iterable):
    return list(map(bool, iterable)).count(True) == 1