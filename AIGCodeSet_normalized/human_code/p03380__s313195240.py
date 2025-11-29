v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sorted(v2, reverse=True)

def f1(a1):
    v1, v2 = (0, v1 - 1)
    while v1 + 1 < v2:
        v3 = (v1 + v2) // 2
        if v3[v3] > a1:
            v1 = v3
        else:
            v2 = v3
    if abs(v3[v1] - a1) >= abs(v3[v1 + 1] - a1):
        v1 += 1
    return v3[v1]

def f2(a1, a2):
    a2 = min(a2, a1 - a2)
    v2 = 1
    for v3 in range(1, a2 + 1):
        v2 *= a1 + 1 - v3
        v2 /= v3
    return int(v2)
v4 = ''
v5 = 0
for v6 in v3[:1]:
    v7 = f1(v6 / 2)
    v4 = str(v6) + ' ' + str(v7)
print(v4)
