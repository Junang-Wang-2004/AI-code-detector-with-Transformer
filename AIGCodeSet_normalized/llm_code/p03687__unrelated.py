def f1(a1):
    v1 = len(a1)
    v2 = v1
    for v3 in range(26):
        v4 = chr(ord('a') + v3)
        v5 = 0
        v6 = 0
        while v6 < v1:
            if a1[v6] == v4:
                v6 += 1
            else:
                v5 += 1
                v6 += 2
        v2 = min(v2, v5)
    return v2
v1 = input()
print(f1(v1))
