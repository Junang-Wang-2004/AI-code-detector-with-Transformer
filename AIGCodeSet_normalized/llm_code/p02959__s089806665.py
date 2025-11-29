v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
for v6, v7 in enumerate(v3):
    if v7 > v2[v6]:
        v5 += min(v7, v2[v6])
        v2[v6 + 1] -= min(v7, v2[v6])
    else:
        v5 += v7
        v2[v6 + 1] -= v7
    if v2[v6 + 1] < 0:
        v4 = 1
        break
print(v5)
