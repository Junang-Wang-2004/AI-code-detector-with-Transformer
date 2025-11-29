import os, sys, re, math
v1, v2 = [int(n) for v3 in input().split()]
v4 = [v3 + 1 for v3 in range(v2)]
for v5 in range(v1):
    v6 = [int(v3) for v3 in input().split()]
    v4 = list(filter(lambda x: x in v6[1:], v4))
print(len(v4))
