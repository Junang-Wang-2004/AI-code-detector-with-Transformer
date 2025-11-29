v1, v2 = list(map(int, input().split()))
v3 = [0] * v2
for v4 in range(v1):
    v5 = list(map(int, input().split()))
    for v6 in v5[1:]:
        v3[v6 - 1] += 1
v7 = 0
for v4 in range(len(v3)):
    if v3[v4] == v1:
        v7 += 1
print(v7)
