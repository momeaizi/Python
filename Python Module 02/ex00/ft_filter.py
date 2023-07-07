

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply):
        raise TypeError('object is not callable')
    if not hasattr(iterable, "__iter__"):
        raise TypeError('object is not iterable')
    
    for iter in iterable:
        if function_to_apply(iter):
            yield iter