v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = [max(v3[0] - v2[0], 0)]
v5 = [max(v2[0] - v3[0], 0)]
for v6 in range(1, v1 - 1):
    v4.append(min(v3[v6], max(v3[v6] + v4[v6 - 1] - v2[v6], 0)))
    v5.append(max(v2[v6] - (v3[v6] + v4[v6 - 1]), 0))
v5.append(max(0, v2[v1 - 1] - v4[-1]))
v7 = sum(v2) - sum(v5)
print(v7)
