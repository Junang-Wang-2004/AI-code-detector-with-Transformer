from itertools import accumulate
v1, v2 = map(int, input().split())
v3 = 0
v4 = [x for v5 in range(v1 + 1)]
v6 = 10 ** 9 + 7
if v2 > v1:
    print(1)
else:
    v7 = list(accumulate(v4))
    v8 = list(accumulate(v4[::-1]))
    v9 = [v4 - b + 1 for v4, v10 in zip(v8, v7)]
    print(sum(v9[v2 - 1:]) % v6)
