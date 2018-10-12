# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def combinations(n):
    # returns all combinations of a + b + c = n where c > b > a
    combos = []
    for c in range(n-2, int(n/3), -1):
        ab = n - c
        for b in range(ab-1, int(ab/2), -1):
            a = ab - b
            if a < b < c:
                combos.append([a, b, c])
    return combos


def is_pythagorean_triplet(a, b, c):
    return a*a + b*b == c*c


n = 1000
for i in combinations(n):
    if is_pythagorean_triplet(*i):
        print(i)
        print(i[0]*i[1]*i[2])