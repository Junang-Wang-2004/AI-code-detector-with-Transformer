v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
v4 = 0
v5 = 1
for v3 in range(1, v1):
    if v2[v3] == v2[v3 - 1]:
        v5 += 1
    else:
        v4 += v5
        v5 = 1
print(v4)
