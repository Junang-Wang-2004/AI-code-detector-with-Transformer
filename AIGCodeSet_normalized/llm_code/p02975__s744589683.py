v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = []
v5 = [0] * 3
for v6 in v2:
    if not v6 in v4:
        v4.append(v6)
    else:
        v5[v4.index(v6)] += 1
    if len(v4) > 3:
        break
if v1 % 3 == 0 and v4[0] ^ v4[2] == v4[1] and (v5[0] == v5[1] and v5[1] == v5[2]) and (len(v4) == 3):
    v3 = 1
if v3 == 1:
    print('Yes')
else:
    print('No')
'01\n10\n11\n01\n10\n11\n\n01\n00\n01\n01\n00\n01\n'
