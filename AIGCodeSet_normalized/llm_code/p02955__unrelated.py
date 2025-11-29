import sys
from typing import List
v1 = sys.stdin.readline
v2, v3 = map(int, v1().split())
v4 = list(map(int, v1().split()))
v5 = sum(v4)
v6 = 1
for v7 in range(1, v5 + 1):
    v8 = sum(((element + v3) % v7 for v9 in v4))
    if v8 % v7 == 0:
        v6 = v7
print(v6)
