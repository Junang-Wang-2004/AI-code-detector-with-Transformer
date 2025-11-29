v1, v2, v3, v4, v5 = map(int, input().split())
v6 = list(map(int, input().split()))
v7 = list(map(int, input().split()))
v8 = list(map(int, input().split()))
v9 = len(v8)
if v9 < v1 + v2:
    max = v9
else:
    max = v1 + v2
v6.sort(reverse=True)
v7.sort(reverse=True)
v8.sort(reverse=True)
v10 = v6[:v1]
v11 = v7[:v2]
v12 = v8[:max]
v10.extend(v11)
v10.sort()
v13 = sum(v10)
for v14 in range(max):
    v15 = v12[v14] - v10[v14]
    if v15 > 0:
        v13 = v13 + v15
    else:
        break
print(v13)
