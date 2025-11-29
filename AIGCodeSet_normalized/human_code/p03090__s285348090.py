v1 = int(input())
v2 = []
v3 = 0
for v4 in range(1, v1):
    for v5 in range(v4 + 1, v1 + 1):
        v2.append([v4, v5])
        v3 += 1
if v1 % 2 == 1:
    for v4 in range(1, v1 // 2 + 1):
        v2.remove([v4, v1 - v4])
        v3 -= 1
else:
    for v4 in range(1, v1 // 2 + 1):
        v2.remove([v4, v1 + 1 - v4])
        v3 -= 1
print(v3)
for v5 in v2:
    print(*v5)
