v1 = list(map(int, input().split()))
v2 = v1[0]
v3 = v1[1]
v4 = list(map(int, input().split()))
v5 = []
for v6 in range(v3):
    v7 = tuple(map(int, input().split()))
    v5.append(v7)

def f1():
    v1 = 0
    for v2 in range(v2):
        if v2 + 1 == v4[v2]:
            v1 += 1
    return v1

def f2(a1, a2, a3):
    a1[a2], a1[a3] = (a1[a3], a1[a2])

def f3():
    v1 = 0
    for v2 in range(v2):
        if v2 + 1 == v4[v2]:
            v1 += 1
    return v1

def f4():
    v1 = f1()
    for v2 in range(v3):
        f2(v4, v5[v2][0] - 1, v5[v2][1] - 1)
        v3 = f3()
        if v3 > v1:
            v1 = v3
        f2(v4, v5[v2][0] - 1, v5[v2][1] - 1)
    return v1
print(f4())
