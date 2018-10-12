# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


counter = 2
i = 3
n = 10001
while counter < n:
    i += 2
    if is_prime(i):
        counter += 1
print(i)
