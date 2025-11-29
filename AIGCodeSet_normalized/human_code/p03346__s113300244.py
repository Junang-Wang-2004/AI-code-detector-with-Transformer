v1 = int(input())
v2 = [0 for v3 in range(v1 + 1)]
for v3 in range(v1):
    v4 = int(input())
    v2[v4] = v2[v4 - 1] + 1
print(v1 - max(v2))
