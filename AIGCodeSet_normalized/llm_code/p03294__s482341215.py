v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v4 = 0
for v5 in range(max(v2)):
    v6 = 0
    for v3 in range(v1):
        v6 += v5 % v2[v3]
    v4 = max(v4, v6)
print(v4)
