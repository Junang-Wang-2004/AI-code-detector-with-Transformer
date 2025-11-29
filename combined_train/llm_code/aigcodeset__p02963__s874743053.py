import sys, re
input = sys.stdin.readline

def f1(a1):
    v1 = [True] * (a1 + 1)
    v1[0] = False
    v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if not v1[v2]:
            continue
        for v3 in range(v2 * 2, a1 + 1, v2):
            v1[v3] = False
    return [v2 for v2 in range(a1 + 1) if v1[v2]]
v1 = int(input())
v2 = [0] * 6
v3 = f1(v1)
if v3:
    pass
else:
    v3.append(1)
for v4 in v3:
    if v1 % v4:
        continue
    else:
        v5 = v1 // v4
        if v5 > 10 ** 9:
            continue
        else:
            v2[2] = v4
            v2[5] = v5
            break
print(' '.join([str(x) for v6 in v2]))
