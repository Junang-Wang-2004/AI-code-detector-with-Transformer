v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = []
for v3, v5 in zip(range(1, v1 + 1), v2):
    v4.append(v5 - v3)
v4.sort()
v6 = v4[v1 // 2]
v7 = 0
for v8 in v4:
    v7 += abs(v8 - v6)
print(v7)
