v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = sum(v2)
v5 = sum(v3)
if v4 > v5:
    print('No')
    exit(0)
v6 = 0
v7 = 0
for v8 in range(v1):
    if v2[v8] < v3[v8]:
        v6 += int((v3[v8] - v2[v8]) / 2)
    else:
        v7 += v2[v8] - v3[v8]
if v6 < v7:
    print('No')
else:
    print('Yes')
