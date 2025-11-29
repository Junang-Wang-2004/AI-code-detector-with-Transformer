v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = {}
for v4 in range(v1):
    if v2[v4] not in v3:
        v3[v2[v4]] = 1
    else:
        v3[v2[v4]] += 1
if len(v3) == 1:
    if v2[0] == 0:
        print('Yes')
        exit()
elif v1 % 3 == 0:
    if len(v3) == 2:
        if 0 in v3:
            if v3[0] == v1 // 3:
                print('Yes')
                exit()
    elif len(v3) == 3:
        v5 = list(v3.keys())
        if v5[0] ^ v5[1] ^ v5[2] == 0:
            if v3[v5[0]] == v1 // 3 and v3[v5[1]] == v1 // 3 and (v3[v5[2]] == v1 // 3):
                print('Yes')
                exit()
print('No')
