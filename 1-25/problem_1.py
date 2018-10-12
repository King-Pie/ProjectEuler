# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from timeit import default_timer as timer


def brute_force(n):
    start = timer()
    multiples = []
    for x in range(n):
        if x % 3 == 0 or x % 5 == 0:
            multiples.append(x)

    answer = sum(multiples)
    end = timer()

    return answer, end - start


def clever_method(n):

    start = timer()

    def triangle_number(n):
        return (n**2 + n) / 2

    n -= 1
    a = 3
    b = 5
    ab = a*b

    answer = float(triangle_number(n/a)*a + triangle_number(n/b)*b - triangle_number(n/ab)*ab)
    end = timer()

    return answer, end - start


n = 1000
print(brute_force(n))
print(clever_method(n))
