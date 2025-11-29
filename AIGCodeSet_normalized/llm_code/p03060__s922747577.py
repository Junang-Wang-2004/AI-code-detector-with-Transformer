v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(v1):
    v6 = v2[v5] - v3[v5]
    if v6 > 0:
        v4 += v6
print(v4)
