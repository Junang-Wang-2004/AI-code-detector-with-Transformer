import itertools
v1, v2, v3 = map(int, input().split())

def f1(a1):
    v1 = 0
    for v2 in range(len(a1)):
        v3 = 0
        for v4 in range(v1 - 1):
            if a1[v2][v4] == a1[v2][v4 + 1]:
                v3 += 1
        if v3 <= v3:
            v1 += 1
    return v1 % 998244353
v4 = [i for v5 in range(1, v2 + 1)]
v6 = v4 * v1
v7 = list(itertools.permutations(v6, v1))
v7 = list(set(v7))
print(f1(v7))
