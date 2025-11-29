def f1(a1, a2):
    v1 = 0
    for v2 in range(a1):
        for v3 in range(v2 + 1, a1):
            if a2[v2:v3] in a2[v3:]:
                v1 = max(v1, v3 - v2)
    return v1
v1 = int(input())
v2 = input()
print(f1(v1, v2))
