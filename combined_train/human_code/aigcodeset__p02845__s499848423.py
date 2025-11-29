import sys
from collections import Counter
v1 = sys.stdin.readline
v2 = int(v1())
v3 = list(map(int, v1().split()))
v4 = 1000000007

def f1(a1):
    v1 = Counter(a1)
    if max(v1.values()) > 3:
        return 0
    v2 = [0] * (v2 + 3)
    v2[-1] = 3
    v3 = 1
    for v4 in a1:
        if v2[v4 - 1] <= 0:
            return 0
        v3 = v3 * v2[v4 - 1] % v4
        v2[v4 - 1] -= 1
        v2[v4] += 1
    return v3
print(f1(v3))
