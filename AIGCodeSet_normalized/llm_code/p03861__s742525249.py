v1 = input()
v1 = v1.split()
v2 = int(v1[0])
v3 = int(v1[1])
v4 = int(v1[2])
v5 = v3 // v4
v6 = (v2 - 1) // v4
if v6 < 0:
    v6 = -1
print(v5 - v6)
