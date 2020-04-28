from math import sqrt
from pprint import pp


def is_prime(x):
    if x <= 2:
        return True

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(is_prime(5))

primes = [x for x in range(1, 100) if is_prime(x)]  # filtering comprehension
print(primes)
prime_square_divisor = {x*x: (1, x, x*x) for x in range(1, 100) if is_prime(x)}
pp(prime_square_divisor)

