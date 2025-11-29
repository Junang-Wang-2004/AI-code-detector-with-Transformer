v1 = input()
v2 = len(v1)
v3 = 0
for v4 in range(v2 // 2):
    if v1[v4] != v1[v2 - v4 - 1]:
        v3 += 1
print(v3)
