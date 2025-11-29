v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = []
v5 = []
for v6 in range(v2):
    v7, v8 = map(int, input().split())
    v4.append(v7)
    v5.append(v8)
v3.sort(reverse=True)
v9 = sum(v3)
for v10 in range(v2 - 1, -1, -1):
    v11 = min(v4[v10], v1)
    v9 += (v5[v10] - v3[v11 - 1]) * v11
    v3 = v3[:v11 - 1] + [v5[v10]] * v11 + v3[v11:]
    v3.sort(reverse=True)
print(v9)
