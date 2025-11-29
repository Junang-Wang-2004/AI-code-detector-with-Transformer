from functools import lru_cache
v1 = int(input())
v2 = int(input())
v3 = [[0] * (v2 + 1) for v4 in range(len(str(v1)) + 1)]

@lru_cache(None)
def f1(a1, a2):
    if a1 < 10:
        if a2 == 0:
            return 1
        if a2 == 1:
            return a1
        else:
            return 0
    if v3[a1][a2] != 0:
        return v3[a1][a2]
    v1 = a1 % 10
    if a2 >= 1:
        v2 = v1 * f1(a1 // 10, a2 - 1) + (9 - v1) * f1(a1 // 10 - 1, a2 - 1)
    else:
        v2 = 0
    v2 += f1(a1 // 10, a2)
    v3[a1][a2] = v2
    return v2
print(f1(v1, v2))
