import math
v1 = int(input())
v2 = math.floor(math.sqrt(v1)) + 1
v3 = [v1]
v4 = [v1 - 1]
for v5 in range(2, v2):
    if v1 % v5 == 0:
        v3.append(v5)
        v6 = v1 // v5
        if v6 == v5:
            continue
        v3.append(v6)
v7 = []
for v5 in v3:
    v8 = v1
    while v8 % v5 == 0:
        v8 = v8 // v5
    if (v8 - 1) % v5 == 0:
        v7.append(v5)
for v5 in range(2, v2):
    if (v1 - 1) % v5 == 0:
        v4.append(v5)
        v6 = (v1 - 1) // v5
        if v6 == v5:
            continue
        v4.append(v6)
v7.extend(v4)
print(len(v7))
