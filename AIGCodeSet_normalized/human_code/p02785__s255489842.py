import sys
sys.setrecursionlimit(10 ** 6)
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
v3 = sorted(v3)[::-1]
if v2 > v1:
    v4 = 0
else:
    if v2 > 0:
        for v5 in range(v2):
            v3[v5] = 0
    v4 = sum(v3)
print(v4)
