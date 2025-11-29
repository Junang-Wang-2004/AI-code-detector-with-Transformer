def f1(a1, a2):
    v1 = 0
    while a1 > 0:
        a1 //= a2
        v1 += 1
    return v1
v1, v2 = map(int, input().split())
print(f1(v1, v2))
