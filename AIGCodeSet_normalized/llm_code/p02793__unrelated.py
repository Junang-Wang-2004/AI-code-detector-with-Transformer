from collections import defaultdict
from math import gcd
v1 = 10 ** 9 + 7

def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = v2[0]
    for v4 in range(1, v1):
        v3 = gcd(v3, v2[v4])
    for v4 in range(v1):
        v2[v4] //= v3
    v5 = defaultdict(int)
    for v4 in range(v1):
        v5[v2[v4]] += 1
    v6 = 0
    for v7, v8 in v5.items():
        v6 = (v6 + v7 * pow(v8, v1 - 2, v1)) % v1
    print(v6)
f1()
