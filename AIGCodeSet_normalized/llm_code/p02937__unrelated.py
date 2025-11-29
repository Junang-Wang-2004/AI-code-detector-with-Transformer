from collections import defaultdict

def f1(a1, a2):
    v1, v2 = (len(a1), len(a2))
    v3 = defaultdict(list)
    for v4, v5 in enumerate(a1):
        v3[v5].append(v4)
    v6 = 0
    v4 = 0
    while v6 < v2:
        if a2[v6] not in v3:
            return -1
        v7 = bisect_left(v3[a2[v6]], v4)
        if v7 == len(v3[a2[v6]]):
            v4 += v1
        else:
            v4 = v3[a2[v6]][v7] + 1
            v6 += 1
    return v4
v1 = input()
v2 = input()
print(f1(v1, v2))
