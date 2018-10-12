# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


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


prime_list = prime_sieve(2e6)
print(sum(prime_list))
