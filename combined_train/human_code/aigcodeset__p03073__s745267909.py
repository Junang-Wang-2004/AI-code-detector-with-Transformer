v1 = [int(x) for v2 in list(input())]
v3 = 0
v4 = 0
for v5 in v1:
    if not v5 == v4:
        v3 += 1
    if v4 == 0:
        v4 = 1
    else:
        v4 = 0
v6 = 0
v4 = 1
for v5 in v1:
    if not v5 == v4:
        v6 += 1
    if v4 == 0:
        v4 = 1
    else:
        v4 = 0
print(min([v3, v6]))
