v1, v2, v3 = map(int, input().split())
v4 = [0] * v2
v5 = 0
for v6 in range(2 ** (v2 - 1)):
    v7 = v6
    v8 = 0
    for v9 in range(v2 - 1):
        if v7 % 2 == v8 == 1:
            break
        v8 = v7 % 2
        v7 = v7 // 2
    else:
        v7 = v6
        for v9 in range(v2 - 1):
            if v7 % 2 == 1:
                v4[v9 + 1] += 1
            v7 = v7 // 2
        v5 += 1

def f1(a1, a2):
    if a1 == v1 + 1:
        return 1
    v1 = max(1, v3 - (v1 - a1))
    v2 = min(v2, v3 + (v1 - a1))
    v3 = 0
    if v1 <= a2 <= v2:
        v3 += (v5 - v4[a2 - 1] - v4[a2]) * f1(a1 + 1, a2)
    if v1 <= a2 - 1 and 1 <= a2 - 1:
        v3 += v4[a2 - 1] * f1(a1 + 1, a2 - 1)
    if a2 + 1 <= v2 and a2 + 1 <= v2:
        v3 += v4[a2] * f1(a1 + 1, a2 + 1)
    return v3 % (10 ** 9 + 7)
print(f1(1, 1))
