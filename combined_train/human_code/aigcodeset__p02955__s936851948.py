def f1(a1, a2):
    return a1 if a1 > a2 else a2

def f2(a1):
    v1 = 1
    v2 = set()
    while v1 * v1 <= a1:
        if not a1 % v1:
            v2.add(v1)
            v2.add(a1 // v1)
        v1 += 1
    v2 = list(v2)
    return v2
import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = sum(v3)
v5 = f2(v4)
v5.sort()
v6 = 0
for v7 in v5:
    v8 = []
    for v9 in v3:
        v8.append(v9 % v7)
    v8.sort()
    v10 = sum(v8) // v7
    if v7 * v10 - sum(v8[-v10:]) <= v2:
        v6 = f1(v6, v7)
print(v6)
