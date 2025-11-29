v1, v2 = map(int, input().split())

def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f2(a1):
    v1 = 2
    v2 = []
    while v1 * v1 <= a1:
        while a1 % v1 == 0:
            a1 = a1 // v1
            v2.append(v1)
        v1 += 1
    if a1 > 1:
        v2.append(a1)
    return list(set(v2))
v3 = f1(v1, v2)
v4 = f2(v3)
print(1 + len(v4))
