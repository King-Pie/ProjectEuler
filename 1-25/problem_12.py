# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?


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


def factors(number):

    prime_list = prime_sieve(int(number/2))

    factor_list = []
    total = 1
    for p in prime_list:
        count = 0
        if number % p == 0:
            while number % p == 0:
                number = int(number/p)
                count += 1
        total *= (count + 1)
        if count != 0:
            factor_list.append((p, count))

    return total


def triangle_number(n):
    return n * ((n+1)/2)


div_n = 1
i = t = 2
while div_n < 500:
    i += 1
    t = triangle_number(i)
    div_n = factors(t)


print(i, t, div_n)
