v1 = int(input())

def f1(a1, a2):
    if a1 - a2 <= 4:
        for v1 in range(a2, a1 + 1):
            if (1 + v1) * v1 / 2 >= v1:
                return v1
    else:
        v2 = int((a1 + a2) // 2)
        if (1 + v2) * v2 / 2 < v1:
            a2 = v2
        else:
            a1 = v2
        return f1(a1, a2)
v2 = f1(v1, 1)
for v3 in range(v2, 0, -1):
    if v1 - v3 >= 0:
        print(v3)
        v1 -= v3
