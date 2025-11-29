import sys
v1 = sys.stdin
sys.setrecursionlimit(10 ** 6)
v2 = lambda: int(ns())
v3 = lambda: list(map(int, v1.readline().split()))
v4 = lambda: list(v1.readline().split())
v5 = lambda: v1.readline().rstrip()
v6 = 10 ** 9 + 7
v7 = int(v5(), 2)
v8 = 0
for v9 in range(v7 // 2):
    for v10 in range(v9 + 1, v7 // 2):
        if v9 ^ v10 == v7:
            v8 += 1
print(v8 % v6)
