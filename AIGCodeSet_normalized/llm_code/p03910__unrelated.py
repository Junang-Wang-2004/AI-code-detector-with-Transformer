v1 = int(input())
v2 = []
v3 = 1
while v1 > 0:
    if v1 >= v3:
        v2.append(v3)
        v1 -= v3
    v3 += 1
for v4 in v2:
    print(v4)
