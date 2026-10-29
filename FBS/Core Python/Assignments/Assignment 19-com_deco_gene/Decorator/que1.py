
def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            print("Result from cache")
            return cache[n]

        result = func(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def square(n):
    print("Calculating...")
    return n * n


print(square(5))
print(square(5))
print(square(4))
