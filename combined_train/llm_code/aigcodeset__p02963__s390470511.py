v1 = int(input())

def f1(a1):
    v1 = 1
    if a1 <= 10 ** 9:
        return a1
    while a1 % 2 == 0:
        a1 //= 2
        v1 *= 2
    if a1 <= 10 ** 9:
        return a1
    v3 = 3
    while v3 * v3 <= a1:
        if a1 // v1 <= 10 ** 9:
            return v1
        if a1 % v3 == 0:
            a1 //= v3
            v1 *= v3
        else:
            v3 += 2
if v1 <= 10 ** 9:
    print(0, 0, 1, 0, 0, v1)
else:
    v2 = f1(v1)
    v3 = v1 // v2
    print(0, 0, v2, 0, 0, v3)
