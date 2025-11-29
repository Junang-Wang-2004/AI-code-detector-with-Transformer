import bisect
v1 = input()
v2 = input()
v3 = len(v1)
v4 = len(v2)
v5 = [[] for v6 in range(28)]

def f1(a1):
    return ord(a1) - 97
for v6 in range(v3):
    v7 = f1(v1[v6])
    v5[v7].append(v6)

def f2():
    v1 = 0
    for v2 in range(v4):
        v3 = v1 % v3
        v4 = f1(v2[v2])
        v5 = v5[v4]
        if len(v5) == 0:
            return -1
        if v2 == 0 and v5[0] == 0:
            v1 = 0
            continue
        if v5[len(v5) - 1] <= v3:
            v1 += v3 - v3
            v3 = -1
        v6 = bisect.bisect_right(v5, v3)
        v7 = v5[v6]
        if v3 != -1:
            v1 += v7 - v3
        else:
            v1 += v7
    return v1 + 1
print(f2())
