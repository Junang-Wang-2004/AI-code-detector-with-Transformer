v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3.append((v5, v6))
v3.sort(key=lambda x: x[1], reverse=True)
v7 = 0
v8 = 0
for v5, v6 in v3:
    while v8 + v5 < v2:
        v7 += 1
        v8 += v5
    v7 += 1
    v8 += v6
print(v7)
