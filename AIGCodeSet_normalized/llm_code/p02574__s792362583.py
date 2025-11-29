v1 = int(input())
v2 = list(map(int, input().split()))
v3 = max(v2)
v4 = [-1] * (v3 + 3)
for v5 in range(2, v3 + 1):
    if v4[v5] != -1:
        continue
    v4[v5] = v5
    v6 = 2
    while v5 * v6 <= v3:
        if v4[v5 * v6] == -1:
            v4[v5 * v6] = v5
        v6 += 1

def f1(a1, a2):
    if v4[a1] == -1:
        return a2
    while a1 > 1:
        a2.append(v4[a1])
        a1 //= v4[a1]
    return a2
v7 = [0] * (v3 + 1)
for v5 in range(v1):
    if v2[v5] == 1:
        continue
    v8 = set(f1(v2[v5], []))
    for v6 in v8:
        v7[v6] += 1
v9 = max(v7)
if v9 == 1:
    print('pairwise coprime')
elif v9 == v1:
    print('not coprime')
else:
    print('setwise coprime')
