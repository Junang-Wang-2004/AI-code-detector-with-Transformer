def f1(a1, a2):
    if a1 == 0:
        return 1 if a2 > 0 else 0
    v1 = (b[a1] + 1) // 2
    if v1 > a2:
        return f1(a1 - 1, a2 - 1)
    elif v1 == a2:
        return p[a1 - 1] + 1
    else:
        return p[a1 - 1] + 1 + f1(a1 - 1, a2 - v1)
v1, v2 = map(int, input().split())
v3 = [1]
v4 = [1]
for v5 in range(v1):
    v3.append(v3[-1] * 2 + 1)
    v4.append(v4[-1] * 2 + 3)
print(f1(v1, v2))
