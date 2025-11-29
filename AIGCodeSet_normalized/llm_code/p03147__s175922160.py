v1 = [0] * n

def f1(a1, a2, a3):
    for v1 in range(a1):
        if a3[v1] < a2[v1]:
            v2 = v1
            break
        elif v1 == a1 - 1 and a3[v1] < a2[v1]:
            v2 = v1
        else:
            v2 = v1 + 1
    for v3 in range(v2, a1):
        if a3[v3] == a2[v3]:
            v4 = v3 - 1
            break
        elif v3 == a1 - 1:
            v4 = v3
    for v5 in range(v2, v4 + 1):
        a3[v5] += 1
v2 = 0
while v1 != h:
    for v3 in range(n):
        if v1[v3] < h[v3]:
            v2 += 1
            f1(n, h, v1)
            break
print(v2)
