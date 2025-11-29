v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
v4 = v1
for v5 in range(v1 - 1, -1, -1):
    if v2[v5] == v4:
        v3 += sorted(v2[v5:v4], reverse=True)
        v4 = v5
v6 = []
for v7 in v3:
    v6.insert(v7 - 1, v7)
if v6 != v2:
    print(-1)
else:
    for v7 in v3:
        print(v7)
