import sys
sys.setrecursionlimit(500005)
v1 = sys.stdin
v2 = lambda: int(ns())
v3 = lambda: list(map(int, v1.readline().split()))
v4 = lambda: v1.readline().rstrip()
v5 = v2()
v6 = v3()
v7 = 0
for v8 in v6:
    v7 ^= v8
v9 = []
for v10 in range(v5):
    v9.append(v6[v10] ^ v7)
print(' '.join(map(str, v9)))
