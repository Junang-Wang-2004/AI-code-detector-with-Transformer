v1 = int(input())
v2 = dict()
for v3 in map(int, input().split()):
    if v2.get(v3) is None:
        v2[v3] = 0
    v2[v3] += 1
print(v1 - sum((min(v2[v3], v3) for v3 in v2)))
