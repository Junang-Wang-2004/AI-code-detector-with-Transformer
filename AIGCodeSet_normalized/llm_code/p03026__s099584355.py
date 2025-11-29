import sys
v1 = sys.stdin
sys.setrecursionlimit(10 ** 7)

def f1():
    return map(int, v1.readline().split())

def f2():
    return map(lambda x: int(x) - 1, v1.readline().split())

def f3():
    return map(float, v1.readline().split())

def f4():
    return v1.readline().split()

def f5():
    return v1.readline().rstrip()

def f6():
    return list(f5())

def f7():
    return int(v1.readline())

def f8():
    return float(v1.readline())
v2 = f7()
v3 = [tuple(f2()) for v4 in range(v2 - 1)]
v5 = list(f1())
v5.sort()
v6 = [[] for v4 in range(v2)]
for v7, v8 in v3:
    v6[v7].append(v8)
    v6[v8].append(v7)
v9 = [i for v10 in range(v2) if len(v6[v10]) == 1]
v11 = [0] * v2
for v10 in range(v2 - 1):
    v12 = v9.pop(0)
    v11[v12] = v5[v10]
    for v13 in v6[v12]:
        v6[v13].remove(v12)
        if len(v6[v13]) == 1:
            v9.append(v13)
v11[v9[0]] = v5[-1]
v14 = 0
for v7, v8 in v3:
    v14 += min(v11[v7], v11[v8])
print(v14)
print(*v11)
