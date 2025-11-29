def f1(a1):
    v1 = 0
    while a1 > 0:
        v2 = 10 ** (len(str(a1)) - 1)
        v1 += a1 // v2
        a1 %= v2
    return v1
v1 = int(input())
print(f1(v1))
