v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
for v6 in range(v1):
    if v2[v6] > v3[v6]:
        v4 += (v2[v6] - v3[v6]) // 2
    else:
        v5 += v3[v6] - v2[v6]
v7 = sum(v2)
v8 = sum(v3)
if v4 + v7 > v8 or v5 > v4:
    print('No')
else:
    print('Yes')
