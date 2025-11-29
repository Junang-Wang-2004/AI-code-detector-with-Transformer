from functools import reduce
from itertools import combinations
v1, v2, v3 = map(int, input().split())
v4 = input()
v5 = range(1, v1 + 1)
v6 = []
for v7, v8 in enumerate(v4, start=1):
    if v8 == 'o':
        continue
    v6.append(v7)
v9 = set(v5) - set(v6)

def f1(a1):
    v1 = a1[1:]
    for v2, v3 in zip(a1, v1):
        if v3 - v2 <= v3:
            return False
    return True
v10 = list(filter(f1, combinations(v9, v2)))
if v10:
    for v7 in sorted(reduce(lambda a, b: set(a) & set(b), v10)):
        print(v7)
