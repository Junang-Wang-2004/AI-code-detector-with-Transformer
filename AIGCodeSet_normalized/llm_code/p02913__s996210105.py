v1 = int(input())
v2 = input()

def f1(a1):
    v1 = len(a1)
    v2 = [0] * v1
    v3 = 1
    v4 = 0
    v2[0] = v5 = len(a1)
    while v3 < v5:
        while v3 + v4 < v5 and a1[v4] == a1[v3 + v4]:
            v4 += 1
        if not v4:
            v3 += 1
            continue
        v2[v3] = v4
        v6 = 1
        while v5 - v3 > v6 < v4 - v2[v6]:
            v2[v3 + v6] = v2[v6]
            v6 += 1
        v3 += v6
        v4 -= v6
    return v2
v3 = 0
for v4 in range(v1):
    for v5 in range(v4 + 1, v1):
        if v2[v4:v4 + v5 - v4 + 1] == v2[v5:v5 + v5 - v4 + 1]:
            v3 = max(v3, v5 - v4 + 1)
print(v3)
