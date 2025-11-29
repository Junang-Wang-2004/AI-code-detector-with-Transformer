v1, v2 = input().split()
v3 = 0
v4 = int(v1[0]) * 10 + int(v1[1])
v5 = int(v1[-2]) * 10 + int(v1[-1])
v6 = int(v2[0]) * 10 + int(v2[1])
v7 = int(v2[-2]) * 10 + int(v2[-1])
if v4 - v5 >= 0:
    v3 += 1
if v6 - v7 >= 0:
    v3 += 1
v3 += (int(v2) - int(v1)) // 100
print(v3)
