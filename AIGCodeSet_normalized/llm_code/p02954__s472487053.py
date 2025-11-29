import sys
input = sys.stdin.readline
v1 = input()
v2 = [0] * len(v1)
v3 = [1] * len(v1)
v4 = [0] * len(v1)
v5 = True
v6 = 0
while v5:
    v6 += 1
    for v7, v8 in enumerate(v1):
        if v8 == 'L':
            if v7 > 0:
                v2[v7 - 1] += v3[v7]
        elif v7 < len(v1) - 1:
            v2[v7 + 1] += v3[v7]
    if v2 == v4:
        v5 = False
    else:
        v4 = v3
        v3 = v2
        v2 = [0] * len(v1)
if v6 % 2 == 0:
    print(*v4)
else:
    print(*v3)
