v1 = input().split()
v2 = len(v1)
v3 = 0
v4 = 0
for v5 in range(v2):
    if v5 % 2 == 0 and v1[v5] != 1:
        v3 += 1
    if v5 % 2 == 1 and v1[v5] != 0:
        v3 += 1
for v5 in range(v2):
    if v5 % 2 == 0 and v1[v5] != 0:
        v4 += 1
    if v5 % 2 == 1 and v1[v5] != 1:
        v4 += 1
print(min(v3, v4))
