v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
v3 = int(input())
v4 = 0
for v5 in range(v3):
    if v1[v5] - v2[v5] > 0:
        v4 += v1[v5] - v2[v5]
print(v4)
