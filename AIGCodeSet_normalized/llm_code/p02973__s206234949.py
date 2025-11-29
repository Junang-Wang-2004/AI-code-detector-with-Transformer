v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
v4 = 1
v5 = v2[0]
for v3 in range(1, v1):
    if v2[v3] > v5:
        v4 += 1
        v5 = v2[v3]
print(v4)
