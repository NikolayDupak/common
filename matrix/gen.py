#!/usr/bin/python3
import sys
import numpy as np

s = 20
if  len(sys.argv) > 1:
    s = int(sys.argv[1])
print(f"Size = {s}")

matrix = np.full((s,s), 1.0, dtype=float)
np.fill_diagonal(matrix, 2.01)

d = np.linalg.det(matrix)
print(f"det = {d}")
np.savetxt("input.txt", matrix, header=f"{s}", comments='', fmt='%.2f', delimiter=' ')