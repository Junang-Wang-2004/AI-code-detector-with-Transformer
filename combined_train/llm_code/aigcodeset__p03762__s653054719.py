v1, v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = 10 ** 9 + 7

def f1(a1, a2):
    return (a1 + a2) % v5

def f2(a1, a2):
    return a1 * a2 % v5

def f3(a1, a2):
    v1 = 0
    for v2 in range(a2):
        v1 = f1(v1, f2(f2(a1[v2], a2 - v2), v2 + 1))
    return v1

def f4(a1, a2):
    v1 = [0] * (a2 - 1)
    for v2 in range(1, a2):
        v1[v2 - 1] = a1[v2] - a1[v2 - 1]
    return v1
v6 = f4(v3, v1)
v7 = f4(v4, v2)
print(f2(f3(v6, v1 - 1), f3(v7, v2 - 1)))
