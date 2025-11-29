import itertools
v1, v2, v3 = map(int, input().split())
v4 = list(range(v2, v3 + 1, 1))
if v1 == 1:
    print(1)
elif v1 == 2:
    print(v3 - v2 + 1)
elif v1 >= 3:
    v5 = list(itertools.combinations_with_replacement(v4, v1 - 2))
    v6 = []
    for v7 in v5:
        v6.append(sum(v7) + v2 + v3)
    v8 = set(v6)
    print(len(v8))
