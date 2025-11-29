import collections as c
from functools import reduce as r
v1 = input()
print(r(lambda x, y: x * y, [i + 1 for v2 in list(c.Counter(input()).values())]) % (10 ** 9 + 7) - 1)
