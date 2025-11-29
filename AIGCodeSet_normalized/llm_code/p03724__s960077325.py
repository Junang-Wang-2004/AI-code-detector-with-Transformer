from collections import defaultdict
import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = [defaultdict(int) for v4 in range(v1)]
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v6 -= 1
    v7 -= 1
    v3[v6][v7] += 1
    v3[v7][v6] += 1
    if v3[v6][v7] == 2:
        v3[v6].pop(v7)
        v3[v7].pop(v6)

def f1(a1, a2, a3):
    for v1 in v3[a1]:
        if v1 != a2:
            v3[v1].pop(a1)
            v3[a1].pop(v1)
            if v1 == a3:
                return -1
            else:
                return f1(v1, a1, a3)
    return -2
for v5 in range(v1):
    if v3[v5]:
        if f1(v5, -1, v5) != -2:
            print('NO')
            exit()
print('YES')
