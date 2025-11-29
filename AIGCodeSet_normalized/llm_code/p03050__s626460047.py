v1 = int(input())
v2 = []
for v3 in range(1, v1 // 2 + 1):
    if v1 // v3 == v1 % v3:
        v2.append(v3)
print(sum(v2))
