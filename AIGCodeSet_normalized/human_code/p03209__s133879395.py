v1, v2 = map(int, input().split())
v3, v4 = ([1], [1])
for v5 in range(v1):
    v3.append(v3[v5] * 2 + 3)
    v4.append(v4[v5] * 2 + 1)

def f1(a1, a2):
    if a1 == 0:
        return 1
    if a2 == 1:
        return 0
    elif 1 < a2 <= v3[a1 - 1] + 1:
        return f1(a1 - 1, a2 - 1)
    elif a2 == v3[a1 - 1] + 2:
        return v4[a1 - 1] + 1
    elif v3[a1 - 1] + 2 < a2 < 2 * v3[a1 - 1] + 2:
        return v4[a1 - 1] + 1 + f1(a1 - 1, a2 - v3[a1 - 1] - 2)
    else:
        return 2 * v4[a1 - 1] + 1
print(f1(v1, v2))
