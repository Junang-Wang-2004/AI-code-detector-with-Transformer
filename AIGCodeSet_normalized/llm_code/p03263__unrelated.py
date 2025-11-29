v1 = int(input())
v2 = int(input())
v3 = []
for v4 in range(v1):
    v3.append(list(map(int, input().split())))

def f1(a1):
    return a1 % 2 == 0

def f2(a1, a2, a3, a4, a5):
    if 0 <= a2 + a4 < v1 and 0 <= a3 + a5 < v2:
        a1[a2 + a4][a3 + a5] += 1
        a1[a2][a3] -= 1

def f3(a1):
    v1 = 0
    for v2 in range(v1):
        for v3 in range(v2):
            if f1(a1[v2][v3]):
                v1 += 1
    return v1

def f4(a1):
    v1 = 0
    for v2 in range(v1):
        for v3 in range(v2):
            if a1[v2][v3] > 0:
                for v4 in range(-1, 2):
                    for v5 in range(-1, 2):
                        if abs(v4) + abs(v5) == 1:
                            f2(a1, v2, v3, v4, v5)
                            v1 += 1
                            if f3(a1) == v1 * v2:
                                return v1
                            f2(a1, v2, v3, -v4, -v5)
    return -1
print(f4(v3))
