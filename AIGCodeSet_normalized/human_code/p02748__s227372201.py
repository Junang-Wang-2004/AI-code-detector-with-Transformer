v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = min(v4) + min(v5)
v7 = []
for v8 in range(v3):
    v9, v10, v11 = map(int, input().split())
    v9 -= 1
    v10 -= 1
    v6 = min(v6, v4[v9] + v5[v10] - v11)
print(v6)
