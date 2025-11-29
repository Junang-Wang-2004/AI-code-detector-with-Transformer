def f1(a1, a2, a3):
    v1 = 0
    for v2 in range(1, a3 + 2):
        if v2 * a1 <= a3 + 0.5:
            v1 += a2
    return v1
v1, v2, v3 = map(int, input().split())
print(f1(v1, v2, v3))
