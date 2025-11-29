v1 = lambda: list(map(int, input().split()))
v2, v3 = v1()
v4 = v1()
v4.sort()
v5 = []
for v6 in range(v3):
    v5.append(v1())
v5.sort(key=lambda x: -x[1])
v7 = []
for v8, v9 in v5:
    if len(v7) >= v2:
        break
    v10 = [int(v9)] * min(v8, v2 - len(v7))
    v7 += v10
v7.sort(reverse=True)
for v11 in range(v2):
    if v7[v11] > v4[v11]:
        v4[v11] = v7[v11]
    else:
        break
v12 = sum(v4)
print(v12)
