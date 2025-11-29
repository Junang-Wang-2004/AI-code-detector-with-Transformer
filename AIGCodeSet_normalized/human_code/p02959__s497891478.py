v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(v1):
    if v3[v5] <= v2[v5]:
        v4 += v3[v5]
    elif v3[v5] <= v2[v5] + v2[v5 + 1]:
        v2[v5 + 1] = v2[v5 + 1] + v2[v5] - v3[v5]
        v4 += v3[v5]
    else:
        v4 += v2[v5] + v2[v5 + 1]
        v2[v5 + 1] = 0
print(v4)
