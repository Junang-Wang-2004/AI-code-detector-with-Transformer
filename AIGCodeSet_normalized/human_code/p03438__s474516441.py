v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
v5 = 0
v6 = 0
for v3 in range(v1):
    if v2[v3] >= v4[v3]:
        v6 += v2[v3] - v4[v3]
    elif (v4[v3] - v2[v3]) % 2 == 0:
        v5 += v4[v3] - v2[v3]
    else:
        v5 += v4[v3] - v2[v3] - 1
if v6 * 2 <= v5:
    print('Yes')
else:
    print('No')
