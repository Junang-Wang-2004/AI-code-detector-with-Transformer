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
v6 = [False] * v2
v7 = [[] for v4 in range(v2)]
for v8, v9 in v3:
    v7[v8].append(v9)
    v7[v9].append(v8)
v10 = 0
v11 = [0] * v2

def f9(a1, a2):
    global cnt
    v6[a1] = True
    for v1 in a2[a1]:
        if not v6[v1]:
            f9(v1, a2)
    v11[a1] = v5[v10]
    v2 += 1
f9(0, v7)
v12 = 0
for v8, v9 in v3:
    v12 += min(v11[v8], v11[v9])
print(v12)
print(*v11)
