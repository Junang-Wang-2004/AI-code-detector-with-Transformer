v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = 0
for v3 in range(v1):
    v4 = v4 ^ v2[v3]
if v4 == 0:
    print('Yes')
else:
    print('No')
