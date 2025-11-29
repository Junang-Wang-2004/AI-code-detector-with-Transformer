from collections import defaultdict

def f1(a1, a2, a3, a4):
    v1 = defaultdict(int)
    for v2 in range(1, a1 - 1):
        for v3 in range(1, a2 - 1):
            v4 = sum(((x, y) in a4 for v5 in range(v2, v2 + 3) for v6 in range(v3, v3 + 3)))
            v1[v4] += 1
    for v3 in range(10):
        print(v1[v3])
v1, v2, v3 = map(int, input().split())
v4 = set((tuple(map(int, input().split())) for v5 in range(v3)))
f1(v1, v2, v3, v4)
