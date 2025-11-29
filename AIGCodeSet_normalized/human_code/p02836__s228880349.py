v1 = input()
v2 = 0
v3 = len(v1) - 1
v4 = 0
while v2 < v3:
    if v1[v2] != v1[v3]:
        v4 += 1
    v2 += 1
    v3 -= 1
print(v4)
