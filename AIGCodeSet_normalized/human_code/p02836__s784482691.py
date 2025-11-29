v1 = input()
v2 = 0
for v3 in range(len(v1) // 2):
    if not v1[v3] == v1[-(v3 + 1)]:
        v2 += 1
print(v2)
