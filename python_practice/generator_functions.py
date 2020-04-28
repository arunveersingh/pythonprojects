def generate123():
    yield 1
    yield 2
    yield 3


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)
    return seen


g = generate123()
print(next(g))
print(next(g))
print(next(g))
print(next(g))