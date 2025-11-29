def f1():
    return int(input())

def f2():
    return map(int, input().split())

def f3():
    return list(f2())

def f4(a1):
    return [f3() for v1 in range(a1)]
v1 = f1()
v2 = f3()
v3 = v2[::2]
v4 = v2[1::2]
v5 = [0]
v6 = [0]
for v7 in v3:
    v5.append(v5[-1] + v7)
for v7 in v4:
    v6.append(v6[-1] + v7)
if v1 % 2 == 0:
    v8 = []
    for v7 in range(v1 // 2 + 1):
        v8.append(v5[v7] + v6[v1 // 2] - v6[v7])
    print(max(v8))
else:
    v9 = []
    for v7 in range((v1 - 1) // 2):
        v9.append(v6[v7 + 1] + v5[(v1 + 1) // 2] - v5[v7 + 2])
    v10 = [0]
    for v7 in v9[::-1]:
        v10.append(max(v10[-1], v7))
    v10 = v10[::-1]
    v11 = v10[0]
    for v7 in range((v1 + 1) // 2):
        v11 = max(v11, v5[v7] + v10[v7] - v6[v7])
    for v7 in v3:
        v11 = max(v11, v5[-1] - v7)
    print(v11)
