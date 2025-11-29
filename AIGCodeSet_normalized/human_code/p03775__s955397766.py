v1 = int(input())
v2 = 11
v3 = 1
while v3 ** 2 <= v1:
    if v1 % v3 == 0:
        v2 = min(v2, len(str(v1 // v3)))
    v3 += 1
print(v2)
