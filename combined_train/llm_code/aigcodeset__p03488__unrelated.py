from collections import defaultdict

def f1(a1, a2, a3):
    v1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    v2 = [0, 0]
    v3 = 0
    v4 = defaultdict(set)
    for v5 in a1:
        if v5 == 'F':
            v2[0] += v1[v3][0]
            v2[1] += v1[v3][1]
        else:
            v3 = (v3 + 1) % 4
        v4[v2[0]].add(v2[1])
    if (a2, a3) in v4:
        return True
    for v6 in range(-len(a1), len(a1) + 1):
        for v7 in range(-len(a1), len(a1) + 1):
            if (a2 - v6, a3 - v7) in v4 and (a2 - v6) % 2 == (a3 - v7) % 2:
                return True
    return False
v1 = input()
v2, v3 = map(int, input().split())
print('Yes' if f1(v1, v2, v3) else 'No')
