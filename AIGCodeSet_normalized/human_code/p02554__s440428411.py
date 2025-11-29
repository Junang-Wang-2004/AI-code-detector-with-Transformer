import sys
import heapq, functools, collections
import random
from collections import Counter, defaultdict
v1 = int(input())
if v1 == 1:
    print(0)
    sys.exit()
v2 = 0
v3 = 10 ** 9 + 7
v4 = pow(10, v1, v3)
v5 = pow(9, v1, v3)
v6 = pow(9, v1, v3)
v7 = pow(8, v1, v3)
print((v4 - v5 - v6 + v7) % v3)
