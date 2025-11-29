def f1(a1, a2, a3, a4):
    v1 = 0
    for v2 in range(a1, a2 + 1):
        if v2 % a3 != 0 and v2 % a4 != 0:
            v1 += 1
    return v1
v1, v2, v3, v4 = map(int, input().split())
print(f1(v1, v2, v3, v4))
