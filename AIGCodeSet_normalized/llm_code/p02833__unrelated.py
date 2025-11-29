def f1(a1):
    if a1 < 2:
        return 0
    v1 = 0
    while a1 >= 5:
        a1 //= 5
        v1 += a1
    return v1
v1 = int(input())
print(f1(v1))
