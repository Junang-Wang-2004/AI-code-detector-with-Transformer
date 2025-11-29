v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v2[0]
v4 = v3
for v5 in range(0, v1):
    if v3 <= v2[v5]:
        v4 += v2[v5] - v3
    v3 = v2[v5]
print(v4)
