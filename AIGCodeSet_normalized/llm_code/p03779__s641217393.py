import itertools
v1 = int(input())
v2 = v1
for v3 in range(1, v1 + 1):
    for v4 in itertools.combinations(range(1, v1 + 1), v3):
        if sum(v4) == v1:
            v2 = min(v2, max(v4))
print(v2)
