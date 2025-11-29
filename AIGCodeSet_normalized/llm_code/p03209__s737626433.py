v1, v2 = map(int, input().split())
v3, v4 = ([1], [1])
for v5 in range(v1):
    v3.append(v3[0] * 2 + 1)
    v4.append(v4[0] * 2 + 3)

def f1(a1, a2):
    if a2 <= 0:
        return 0
    elif a1 <= 0:
        return min(a2, 3)
    elif a2 > v4[a1]:
        return v3[a1] + 1 + f1(a1 - 1, a2 - 2 - v4[a1])
    elif a2 == v4[a1]:
        return v3[a1]
    else:
        return f1(a1 - 1, a2 - 1)
print(f1(v1, v2))
