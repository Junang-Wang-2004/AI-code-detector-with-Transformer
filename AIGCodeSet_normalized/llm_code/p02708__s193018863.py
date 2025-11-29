import itertools
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2, v1 + 2):
    for v5 in itertools.combinations(range(10 ** 100, 10 ** 100 + v1 + 1), v4):
        v3.add(sum(v5))
print(len(set(v3)) % (10 ** 9 + 7))
