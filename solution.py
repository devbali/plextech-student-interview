def is_one_to_one(iterable1, iterable2):
    mapping = {}
    b_elements = []
    iter2 = iter(iterable2)
    for a in iterable1:
        try:
            b = next(iter2)
        except StopIteration:
            raise OverflowError("Iterables of unequal length")

        if a in mapping:
            if b != mapping[a]: return False
        elif b in b_elements: return False
        else:
            mapping[a] = b
            b_elements.append(b)
    try:
        next(iter2)
        raise OverflowError("Iterables of unequal length")
    except StopIteration:
        return True
