v1 = input()
v2, v3 = list(map(int, input().split()))
v4 = []
v5 = []
v6 = 0
for v7 in v1:
    if v7 == 'T':
        (v4 if len(v4) == len(v5) else v5).append(v6)
        v6 = 0
    else:
        v6 += 1
(v4 if len(v4) == len(v5) else v5).append(v6)
v1 = v4[0]
v8 = 0
v4 = sorted(v4[1:], reverse=True)
v5 = sorted(v5, reverse=True)
for v7 in v4:
    v1 += v7 * (-1 if v1 > v2 else 1)
for v7 in v5:
    v8 += v7 * (-1 if v8 > v3 else 1)
if v1 == v2 and v8 == v3:
    print('Yes')
else:
    print('No')
