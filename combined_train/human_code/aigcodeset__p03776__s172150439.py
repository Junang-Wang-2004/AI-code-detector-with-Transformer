v1 = {}

def f1(a1, a2):
    if a2 == 0 or a2 == a1:
        return 1
    if a2 == 1:
        return a1
    if (a1, a2) in v1:
        return v1[a1, a2]
    v1[a1, a2] = f1(a1 - 1, a2) + f1(a1 - 1, a2 - 1)
    return v1[a1, a2]
v2, v3, v4 = map(int, input().split())
v5 = sorted(list(map(int, input().split())), reverse=True)
'\nif len(set(v)) == 1:\n    print(1)\n    print(1125899906842623)\n    exit()\n'
v6 = sum(v5[:v3]) / v3
print(v6)
if len(set(v5[:v3])) == 1:
    v7 = 0
    v8 = v5.count(v5[0])
    for v9 in range(v3, v4 + 1):
        if v9 <= v8:
            v7 += f1(v8, v9)
    print(v7)
    exit()
v10 = min(v5[:v3])
v11 = v5[:v3].count(v10)
v6 = v5.count(v10)
print(f1(v6, v11))
