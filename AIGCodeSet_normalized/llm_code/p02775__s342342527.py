v1 = input()
v2 = 0
for v3 in range(len(v1)):
    v4 = int(v1[v3])
    if v4 == 1:
        v2 += 1
    else:
        v2 += v4
print(v2)
