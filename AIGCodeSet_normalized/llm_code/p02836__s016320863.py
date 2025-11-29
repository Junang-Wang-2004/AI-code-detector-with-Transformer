v1 = input()
v2 = len(v1) // 2
v3 = 0
for v4 in range(v2):
    if v1[v4] != v1[len(v1) - v4 - 1]:
        v3 += 1
print(v3)
