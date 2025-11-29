v1 = int(input())
v2 = list(input())
v3 = 1000000007
if v1 == 1:
    print(3)
    exit(0)
v4 = []
v5 = False
for v6 in range(v1 - 1):
    if v5:
        v5 = False
        continue
    if v2[v6] == v2[v6 + 1]:
        v4.append(2)
        v5 = True
    else:
        v4.append(1)
if v4[0] == 1:
    v7 = 3
else:
    v7 = 6
for v6 in range(1, len(v4)):
    if v4[v6 - 1] == 1:
        v7 = v7 * 2 % v3
    elif v4[v6] == 2:
        v7 = v7 * 3 % v3
    else:
        v7 = v7 * 2 % v3
print(v7)
