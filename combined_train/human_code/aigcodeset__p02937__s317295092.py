import sys

def f1():
    return sys.stdin.readline().strip()

def f2():
    v1 = f1()
    v2 = f1()
    import collections
    v3 = collections.defaultdict(list)
    for v4, v5 in enumerate(v1):
        v3[v5].append(v4)
    v6 = v3.keys()
    for v5 in set(v2):
        if v5 not in v6:
            print(-1)
            return
    import bisect
    v7 = 0
    v8 = -1
    for v5 in v2:
        v9 = v3[v5]
        v10 = bisect.bisect_right(v9, v8)
        if v10 >= len(v9):
            v7 += 1
            v8 = v9[0]
        else:
            v11 = v9[v10]
            v8 = v11
    print(len(v1) * v7 + v8 + 1)
f2()
