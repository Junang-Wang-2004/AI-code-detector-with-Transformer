import sys
v1 = 0
v2 = [input().split() for v3 in sys.stdin]
v4 = [int(x[0]) for v5 in v2]
v6 = v4.index(min(v4))
for v7 in v2[v6][1:]:
    v8 = sum([int(v5) for v5 in v2[i][1:] if int(v5) == int(v7) for v9 in range(len(v2))])
    if v8 == len(v4):
        v1 = v1 + 1
print(v1)
