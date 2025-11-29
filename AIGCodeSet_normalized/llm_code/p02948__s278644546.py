v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append([int(i) for v5 in input().split()])
v3 = sorted(v3)

def f1(a1, a2, a3, a4):
    if a2 == len(a1):
        return 0
    if a3 > v2:
        return 0
    if (a2, a3) in a4:
        return a4[a2, a3]
    v1 = f1(a1, a2 + 1, a3 + a1[a2][0], a4) + a1[a2][1]
    v2 = f1(a1, a2 + 1, a3, a4)
    a4[a2, a3] = max(v1, v2)
    return a4[a2, a3]
v6 = 0
for v5 in range(len(v3)):
    if v3[v5][0] > v2:
        v6 += 1
if v6 == len(v3):
    print(0)
else:
    v7 = {}
    print(f1(v3, 0, 1, v7))
