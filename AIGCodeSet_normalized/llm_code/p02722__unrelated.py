v1 = int(input())
v2 = 0
for v3 in range(2, v1 + 1):
    v4 = v1
    while v4 >= v3:
        if v4 % v3 == 0:
            v4 = v4 // v3
        else:
            v4 = v4 - v3
        if v4 == 1:
            v2 += 1
            break
print(v2)
