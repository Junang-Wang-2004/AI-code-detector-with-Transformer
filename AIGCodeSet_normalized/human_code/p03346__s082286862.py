v1 = int(input())
v2 = [0] * v1
for v3 in range(0, v1):
    v4 = int(input())
    v2[v4 - 1] = v3
v5 = 1
v6 = 1
for v3 in range(1, v1):
    if v2[v3] > v2[v3 - 1]:
        v5 = v5 + 1
        v6 = max(v6, v5)
    else:
        v5 = 1
print(v1 - v6)
