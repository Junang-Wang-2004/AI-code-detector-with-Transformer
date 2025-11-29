def f1(a1: list):
    v1 = 0
    for v2 in range(1, len(a1) - 1):
        v3 = int(a1[v2 - 1])
        v4 = int(a1[v2])
        v5 = int(a1[v2 + 1])
        if v3 < v4 < v5 or v3 > v4 > v5:
            v1 += 1
    return v1
v1 = input()
v2 = input()
v3 = f1(v2.split())
print(v3)
