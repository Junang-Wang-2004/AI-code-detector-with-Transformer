v1, v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v5 = int(input())
    v3.append(v5)
v3.sort()
min = 1000000000
for v6 in range(v1 - v2 + 1):
    v7 = v3[v6 + v2 - 1] - v3[v6]
    if v7 < min:
        min = v7
print(min)
