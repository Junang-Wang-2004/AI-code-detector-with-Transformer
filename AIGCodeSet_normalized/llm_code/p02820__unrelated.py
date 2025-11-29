def f1(a1, a2, a3, a4, a5, a6):
    v1 = [0] * (a1 + 1)
    for v2 in range(1, a1 + 1):
        v1[v2] = max(v1[v2], v1[v2 - 1])
        if v2 >= a2:
            if a6[v2 - 1] == 'r' and a6[v2 - a2 - 1] != 'p':
                v1[v2] = max(v1[v2], v1[v2 - a2] + a5)
            if a6[v2 - 1] == 'p' and a6[v2 - a2 - 1] != 's':
                v1[v2] = max(v1[v2], v1[v2 - a2] + a4)
            if a6[v2 - 1] == 's' and a6[v2 - a2 - 1] != 'r':
                v1[v2] = max(v1[v2], v1[v2 - a2] + a3)
    return v1[a1]
v1, v2 = map(int, input().split())
v3, v4, v5 = map(int, input().split())
v6 = input()
print(f1(v1, v2, v3, v4, v5, v6))
