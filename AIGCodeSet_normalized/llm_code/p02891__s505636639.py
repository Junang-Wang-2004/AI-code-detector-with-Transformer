v1 = input()
v2 = int(input())
v3 = v1 * 2
v4 = 0
v5 = 0
for v6 in range(1, len(v1)):
    if v1[v6 - 1] == v1[v6]:
        v4 += 1
for v6 in range(1, len(v3)):
    if v3[v6 - 1] == v3[v6]:
        v5 += 1
print(v4 + v5 * (v2 - 1))
