import itertools
v1, v2, v3 = map(int, input().split())
v4 = 0
for v5 in range(1, v1 + 1):
    if v5 == v2 or v5 == v3:
        continue
    else:
        v4 += len(list(itertools.combinations(range(v1), v5)))
print(v4 % (10 ** 9 + 7))
