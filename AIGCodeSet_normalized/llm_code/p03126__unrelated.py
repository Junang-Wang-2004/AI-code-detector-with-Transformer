from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = defaultdict(set)
for v4 in range(v1):
    v5 = list(map(int, input().split()))
    for v6 in v5[1:]:
        v3[v6].add(v4)
v7 = set((v6 for v6, v5 in v3.items() if len(v5) == v1))
print(len(v7))
