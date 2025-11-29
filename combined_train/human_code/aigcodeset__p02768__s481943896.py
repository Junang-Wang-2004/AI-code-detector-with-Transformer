v1 = 10 ** 9 + 7

def f1(a1, a2):
    return (a1 + a2) % v1

def f2(a1, a2):
    return (a1 + v1 - a2) % v1

def f3(a1, a2):
    return a1 % v1 * (a2 % v1) % v1

def f4(a1, a2):
    if a2 == 0:
        return 1
    elif a2 == 1:
        return a1 % v1
    elif a2 % 2 == 0:
        return f4(a1, a2 // 2) ** 2 % v1
    else:
        return f4(a1, a2 // 2) ** 2 * a1 % v1

def f5(a1, a2):
    return f3(a1, f4(a2, v1 - 2))
v2, v3, v4 = map(int, input().split())
v5 = f4(2, v2)
v5 = f2(v5, 1)
v6 = 1
v7 = 1
for v8 in range(v3):
    v6 = f3(v6, v2 - v8)
    v7 = f3(v7, v8 + 1)
v6 = f5(v6, v7)
v9 = 1
v10 = 1
for v8 in range(v4):
    v9 = f3(v9, v2 - v8)
    v10 = f3(v10, v8 + 1)
v9 = f5(v9, v10)
v5 = f2(v5, v6)
v5 = f2(v5, v9)
print(v5)
