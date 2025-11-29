from collections import Counter

def f1(a1: int, a2: int) -> list:
    v1 = [-1, 1]
    for v2 in range(2, a1 + 1):
        v1.append(a2 - a2 // v2 * v1[a2 % v2] % a2)
    return v1

def f2(a1: int, a2: int) -> list:
    v1 = [1, 1]
    v2 = 1
    for v3 in range(2, a1 + 1):
        v2 = v2 * v3 % a2
        v1.append(v2)
    return v1

def f3(a1: int, a2: list, a3: int) -> list:
    v1 = [1, 1]
    for v2 in range(2, a1 + 1):
        v1.append(v1[v2 - 1] * a2[v2] % a3)
    return v1

def f4(a1: int, a2: int, a3: int, a4: list, a5: list) -> int:
    if not (0 <= a2 and a2 <= a1):
        return 0
    return a4[a1] * a5[a2] % a3 * a5[a1 - a2] % a3
v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v4.sort(reverse=True)
v5 = sum(v4[:v2]) / v2
print(v5)
v6 = 9999999900000001
v7 = f1(v1, v6)
v8 = f2(v1, v6)
v9 = f3(v1, v7, v6)
v10 = Counter(v4)
v11 = 0
if len(v10) == 1:
    for v12 in range(v2, v3 + 1):
        v11 += f4(v1, v12, v6, v8, v9)
    print(v11)
else:
    v13 = v4[:v3].count(v4[v2 - 1])
    v14 = v4.count(v4[v2 - 1])
    for v12 in range(v13, v14 + 1):
        v11 += f4(v14, v12, v6, v8, v9)
    print(v11)
