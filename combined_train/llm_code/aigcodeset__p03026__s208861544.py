v1 = int(input())
abs = [] * v1
for v2 in range(v1 - 1):
    abs.append(list(map(int, input().split())))
v3 = list(map(int, input().split()))
v4 = [0] * v1
for v2 in range(v1 - 1):
    v5 = max(v4[abs[v2][0] - 1], v4[abs[v2][1] - 1])
    v5 += 1
    v4[abs[v2][0] - 1] = v5
    v4[abs[v2][1] - 1] = v5
for v2 in range(v1 - 1):
    v5 = max(v4[abs[v2][0] - 1], v4[abs[v2][1] - 1])
    v4[abs[v2][0] - 1] = v5
    v4[abs[v2][1] - 1] = v5
v6 = [0] * v1
for v2 in range(v1):
    v6[v4.index(max(v4))] = max(v3)
    v4[v4.index(max(v4))] = 0
    v3[v3.index(max(v3))] = 0
print(sum(v6))
print(*v6)
