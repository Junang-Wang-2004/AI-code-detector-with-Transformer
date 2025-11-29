from math import ceil
from sys import stdin
v1 = int(stdin.readline().rstrip())
v2 = [int(_) for v3 in stdin.readline().rstrip().split()]
v4 = 10 ** 10
for v5 in range(v1 - 1):
    v4 = min(v4, abs(sum(v2[:v5 + 1]) - 2 * v2[v5]))
print(v4)
