v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = [0] * v1
v5 = 0
for v6 in range(v1):
    v4[v6] = v2[v6] - v3[v6]
for v6 in range(v1):
    if v4[v6] >= 0:
        v5 += v4[v6]
print(v5)
