# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def is_prime(n):

    for i in range(2, n/2):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n):

    # if even, largest prime factor is 2
    if n % 2 == 0:
        return 2

    i = 3
    while i < n:
        # is i a factor?
        if n % i == 0:
            if is_prime(i):
                n = n/i
        i += 2
    return n


print largest_prime_factor(600851475143)
