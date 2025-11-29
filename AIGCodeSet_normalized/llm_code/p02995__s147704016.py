def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1
v1, v2, v3, v4 = map(int, input().split())
v5 = v3 * v4 // f1(v3, v4)
print(v2 - v1 + 1 - int(v2 / v3) + int(v1 / v3) - int(v2 / v4) + int(v1 / v4) + int(v2 / v5) - int(v1 / v5))
