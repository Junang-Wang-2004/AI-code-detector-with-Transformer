v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(input())
v4 = 0
v5 = 0
v6 = 0
v7 = 0
for v3 in range(v1):
    if v2[v3][-1].count('A') and v2[v3][0].count('B'):
        v7 += 1
    else:
        v4 += v2[v3][-1].count('A')
        v5 += v2[v3][0].count('B')
    v6 += v2[v3].count('AB')
if v7 != 0:
    v6 += v7 - 1
    if v4 > v5:
        v5 += 1
    elif v5 > v4:
        v4 += 1
    elif v4 == v5 and v4 >= 1:
        v4 += 1
        v5 += 1
print(v6 + min(v4, v5))
