v1 = int(input())
v2 = [i for v3 in map(int, input().split())]
v4 = 1
for v3 in range(v1 - 1, 0, -1):
    if v2[v3 - 1] > v2[v3]:
        v2[v3 - 1] -= 1
for v3 in range(1, v1 - 1):
    if not v2[v3 - 1] <= v2[v3] <= v2[v3 + 1]:
        v4 = 0
        break
if v4:
    print('Yes')
else:
    print('No')
