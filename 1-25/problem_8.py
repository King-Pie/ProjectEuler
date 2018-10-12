# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

path = '../data/problem_8_data.txt'

data = []
with open(path) as file:
    temp = file.read().splitlines()
number = (''.join(temp))

products = []
for i in range(0, 1001-13):
    seq = ([int(x) for x in list(number[i:i+13])])
    prod = 1
    for j in seq:
        prod *= int(j)

    products.append(prod)

print(max(products))
