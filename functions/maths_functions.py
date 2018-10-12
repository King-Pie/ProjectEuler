# Selection of mathematical functions


def is_prime(n):
    """
    General function to test if n is a prime number
    :param n: number to test
    :return: True/False if n is/isn't prime
    """

    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_sieve(limit):

    a = [True] * int(limit)
    a[0] = a[1] = False
    prime_list = []
    for (i, isprime) in enumerate(a):
        if isprime:
            prime_list.append(i)
            for n in range(i*i, int(limit), i):
                a[n] = False

    return prime_list


if __name__ == '__main__':

    print(prime_sieve(2e6))


