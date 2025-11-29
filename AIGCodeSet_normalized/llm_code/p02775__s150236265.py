v1 = input()
v2 = 5 * len(v1)
v2 -= abs(5 - int(v1[0]))
v3 = int(v1[0])
v4 = True
for v5 in range(1, len(v1)):
    v6 = int(v1[v5])
    v2 -= abs(v6 - 5)
    if v4:
        if v3 <= 4 and v6 >= 6 or (v3 >= 6 and v6 <= 4):
            v2 += 1
            v4 = False
    else:
        v4 = True
    v3 = v6
print(v2)
