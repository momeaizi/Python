from functools import reduce

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError('object is not callable')
    if not hasattr(iterable, "__iter__"):
        raise TypeError('object is not iterable')
    if len(iterable) == 0:
        raise TypeError('reduce() of empty iterable')
    
    ans = None
    for iter in iterable:
        if ans is None:
            ans = iter
            continue
        ans = function_to_apply(ans, iter)
    
    return ans

