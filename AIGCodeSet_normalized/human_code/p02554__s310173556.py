v1 = int(1000000000.0 + 7)

def f1(a1, a2):
    v1 = 1
    while a2:
        if a2 % 2:
            v1 = v1 * a1 % v1
        a1 = a1 * a1 % v1
        a2 //= 2
    return v1
v2 = int(input())
print((2 * (f1(10, v2) - f1(9, v2)) - (f1(10, v2) - f1(8, v2))) % v1)
