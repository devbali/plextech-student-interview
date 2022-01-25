"""
Task:

A "One to One" relationship is one where every unique element of iterable1 can be subbed for some other to get iterable2.

For example, "hell" and "miss" are one to one, since if you start with "hell" and replace every h with m, e with i, and l with s, you get miss
Similarly, [1,2,3,2] and [1,4,2,4] are one to one, but [1,2,3,2] and [1,2,3,4] are not
If the two iterables have different lengths, raise an OverflowError with the message "Iterables of unequal length"
But you should not use the len() function, since you only know these are iterables. 
NOTE: *Do not use list() or tuple() or try converting types*
Hint:
    You can use for .. in .. with iterables, and use iter(iterable) to turn an iterable into an iterator
    a = iter("he")
    next(a) # h
    next(a) # e
    next(a) # StopIteration Exception
"""

def array_to_generator_iterable (array):
    # Testing Function: Converts an array into an iterable onto which you can not call len()
    yield from array

def is_one_to_one(iterable1, iterable2):
    """Return if iterable1 and iterable2 are "One to One" as defined above
    Examples with String:
    >>> is_one_to_one("hell","miss")
    True
    >>> is_one_to_one("hill","sass")
    False
    >>> is_one_to_one("hello","miss")
    Traceback (most recent call last):
        ...
    OverflowError: Iterables of unequal length

    Examples with lists:
    >>> a = [1,2,3,2]
    >>> b = [1,4,2,4]
    >>> c = [1,2,3,4]
    >>> d = [1,2,3,2,5,6]
    >>> is_one_to_one(a,b)
    True
    >>> is_one_to_one(a,c)
    False
    >>> is_one_to_one(a,d)
    Traceback (most recent call last):
        ...
    OverflowError: Iterables of unequal length
    >>> is_one_to_one(d,a)
    Traceback (most recent call last):
        ...
    OverflowError: Iterables of unequal length
    
    The same as previous, if you use iterable functions, and not functions like len():
    >>> is_one_to_one(array_to_generator_iterable(a),array_to_generator_iterable(b))
    True
    >>> is_one_to_one(array_to_generator_iterable(a),array_to_generator_iterable(c))
    False
    >>> is_one_to_one(array_to_generator_iterable(a),array_to_generator_iterable(d))
    Traceback (most recent call last):
        ...
    OverflowError: Iterables of unequal length
    >>> is_one_to_one(array_to_generator_iterable(d),array_to_generator_iterable(a))
    Traceback (most recent call last):
        ...
    OverflowError: Iterables of unequal length
    """
    pass ### YOUR CODE HERE

if __name__ == "__main__":
    import doctest
    doctest.testmod()
