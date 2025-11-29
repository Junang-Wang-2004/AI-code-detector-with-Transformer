from collections import defaultdict

def f1(a1, a2):
    v1 = defaultdict(int)
    for v2, v3 in a2:
        v1[v2, v3] += 1
    v4 = float('inf')
    for v5 in range(-10 ** 9, 10 ** 9 + 1):
        for v6 in range(-10 ** 9, 10 ** 9 + 1):
            if v5 == 0 and v6 == 0:
                continue
            v7 = 0
            for v2, v3 in a2:
                if (v2 - v5, v3 - v6) not in v1:
                    v7 += 1
                v1[v2, v3] -= 1
                if v1[v2, v3] == 0:
                    del v1[v2, v3]
            v4 = min(v4, v7)
            v1 = defaultdict(int)
            for v2, v3 in a2:
                v1[v2, v3] += 1
    return v4
v1 = int(input())
v2 = [tuple(map(int, input().split())) for v3 in range(v1)]
print(f1(v1, v2))
