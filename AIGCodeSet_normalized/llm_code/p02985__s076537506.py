v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1 - 1):
    v3.append(list(map(int, input().split())))
v5 = [1]
v6 = [0] * v1

def f1(a1, a2):
    v1 = []
    for a1 in v3:
        if a1[0] == a2 and v6[a1[1] - 1] == 0:
            v1.append(a1[1])
        elif a1[1] == a2 and v6[a1[0] - 1] == 0:
            v1.append(a1[0])
    return v1

def f2(a1, a2):
    v1 = []
    v2 = f1(a1, a2)
    for v3 in v2:
        v4 = f1(a1, v3)
        v1.extend(v4)
    v2.extend(v1)
    v2 = list(set(v2))
    if a2 in v2:
        v2.remove(a2)
    return v2

def f3(a1, a2):
    v1 = []
    for a1 in v3:
        if a1[0] == a2 and v6[a1[1] - 1] != 0:
            v1.append(a1[1])
        elif a1[1] == a2 and v6[a1[0] - 1] != 0:
            v1.append(a1[0])
    return v1

def f4(a1, a2):
    v1 = []
    v2 = f3(a1, a2)
    for v3 in v2:
        v4 = f3(a1, v3)
        v1.extend(v4)
    v2.extend(v1)
    return v2 - len(set(v2))
while v5:
    v7 = v5.pop(0)
    v6[v7 - 1] = f4(v3, v7)
    v5.extend(f2(v3, v7))
    v5 = list(set(v5))
v8 = 1
for v4 in v6:
    v8 = v8 * v4 % 1000000007
print(v8)
