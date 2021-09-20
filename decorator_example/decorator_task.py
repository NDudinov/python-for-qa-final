import time


def cache_decorator_bool(arg):
    if arg:
        def cache_decorator(func):
            cache = {}

            def cache_func(x):
                if x in cache:
                    print(f"{cache[x][1]} Cache hit for number {x}")
                    return cache[x][0]
                else:
                    val = func(x)
                    t = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime())
                    cache[x] = val, t
                    return val
            return cache_func
        return cache_decorator
    else:
        def just_decorator(func):
            return func
        return just_decorator


@cache_decorator_bool(True)
def factorial(n):
    if n < 2:
        return 1
    return factorial(n - 1) * n




