v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]

def f1(a1):
    return ord(a1) - ord('a')
if v1 % 2 == 0:
    if v2 % 2 == 0:
        v5 = 1
    else:
        v5 = 2
elif v2 % 2 == 0:
    v5 = 3
else:
    v5 = 4
v6 = [0] * 26
for v4 in range(v1):
    for v7 in range(v2):
        v6[f1(v3[v4][v7])] += 1
v8 = 0
v9 = 0
for v4 in range(26):
    if v6[v4] % 2 == 1:
        v10 = v6[v4]
        if v10 % 4 == 3:
            v9 += 1
        v8 += 1
    elif v6[v4] % 2 == 0 and v6[v4] % 4 != 0:
        v9 += 1
if v8 > 1:
    print('No')
    exit()
elif v5 == 1:
    if v9 > 0:
        print('No')
        exit()
elif v5 == 2:
    if v9 > v1 // 2:
        print('No')
        exit()
elif v5 == 3:
    if v9 > v2 // 2:
        print('No')
        exit()
elif v5 == 4:
    if v9 > (v1 + v2 - 2) // 2:
        print('No')
        exit()
print('Yes')
