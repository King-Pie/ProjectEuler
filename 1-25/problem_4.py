# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# largest product of two three digit numbers is 998001


def is_palindromic(n):
    nstring = str(n)
    half = int(len(nstring)/2)

    return nstring[:half] == nstring[-half:][::-1]


def largest_palindrome():
    for i in range(998001, 10000, -1):
        if is_palindromic(i):
            for j in range(1000, 100, -1):
                if i % j == 0:
                    if 100 < i/j < 1000:
                        return j, i/j, i


print(largest_palindrome())
