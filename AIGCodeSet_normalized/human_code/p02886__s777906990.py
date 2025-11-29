from functools import reduce
from itertools import accumulate
from math import gcd
v1 = int(input())
v2 = list(map(int, input().split()))
print(sum((d * cumulate for v3, v4 in zip(v2[1:], accumulate(v2)))))
