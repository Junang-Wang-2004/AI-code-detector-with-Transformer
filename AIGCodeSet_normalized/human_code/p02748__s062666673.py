v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = []
for v7 in range(v3):
    v8, v9, v10 = map(int, input().split())
    v8 -= 1
    v9 -= 1
    v6.append(v4[v8] + v5[v9] - v10)
v6.sort()
print(min(min(v4) + min(v5), v6[0]))
