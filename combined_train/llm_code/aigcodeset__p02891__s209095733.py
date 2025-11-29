v1 = input()
v2 = int(input())
v3 = 0
v4 = 0
for v5 in range(1, len(v1)):
    if v4 == 0 and v1[v5 - 1] == v1[v5]:
        v3 += 1
        v4 = 1
    else:
        v4 = 0
v6 = 0
v7 = 1
for v5 in range(1, len(v1)):
    if v7 == 0 and v1[v5 - 1] == v1[v5]:
        v6 += 1
        v7 = 1
    else:
        v7 = 0
if v2 % 2 == 0:
    print(v2 * min(v3, v6))
else:
    print(v2 * v3)
