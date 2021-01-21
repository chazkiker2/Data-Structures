def memoize(func):
    """Reusable memoization decorator

    For any function that uses this decorator, that function will cache results here.
    When the decorated function gets called, if the parameters are already in the cache we can return
    the result from cache instead of re-computing.
    """
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
