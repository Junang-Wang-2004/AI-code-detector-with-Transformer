v1 = int(input())
v2 = list(map(int, input().split(' ')))
v3 = list(map(int, input().split(' ')))
v4 = list(map(int, input().split(' ')))
v5 = 0
for v6 in range(v1 - 1):
    v5 += v3[v2[v6] - 1]
    if v2[v6 + 1] == v2[v6] + 1:
        v5 += v4[v2[v6] - 1]
v5 += v3[v2[v1 - 1] - 1]
print(v5)
