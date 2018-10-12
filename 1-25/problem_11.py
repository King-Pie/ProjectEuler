# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

import numpy as np

path = '../data/problem_11_data.txt'

data = []
with open(path) as file:
    for line in file:
        data.append(line.rsplit())

data = np.array(data)


sequence_list = []
product_list = []

# horizontal sequences
for i in range(0, 20-3):
    for j in range(0, 20):
        seq = [int(x) for x in data[j, i:i+4]]
        sequence_list.append(seq)
        prod = 1
        for s in seq:
            prod *= int(s)
        product_list.append(prod)

# vertical sequences
for i in range(0, 20):
    for j in range(0, 20-3):
        seq = [int(x) for x in data[j:j+4, i]]
        sequence_list.append(seq)
        prod = 1
        for s in seq:
            prod *= int(s)
        product_list.append(prod)

# diagonal sequences 1
for i in range(0, 20-3):
    for j in range(0, 20-3):
        seq = [data[i, j], data[i+1, j+1], data[i+2, j+2], data[i+3, j+3]]
        seq = [int(x) for x in seq]
        sequence_list.append(seq)
        prod = 1
        for s in seq:
            prod *= int(s)
        product_list.append(prod)

# diagonal sequences 2
for i in range(3, 20):
    for j in range(0, 20-3):
        seq = [data[i-3, j+3], data[i-2, j+2], data[i-1, j+1], data[i, j]]
        seq = [int(x) for x in seq]
        sequence_list.append(seq)
        prod = 1
        for s in seq:
            prod *= int(s)
        product_list.append(prod)

m = max(product_list)
idx = [i for i, j in enumerate(product_list) if j == m][0]

print(sequence_list[idx], product_list[idx])
