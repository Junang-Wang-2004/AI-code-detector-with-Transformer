v1 = int(input())
if v1 <= 2:
    print(v1)
    exit()
v2 = 1
v3 = 500000000
while True:
    if v1 - v2 * (v2 + 1) // 2 >= v2 + 1:
        v3 = min(v3, v1 - v2 * (v2 + 1) // 2)
    if v2 * (v2 + 1) > 2 * v1:
        break
    v2 += 1
v4 = abs(v2 * (v2 + 1) // 2 - v1)
v5 = abs(v2 * (v2 - 1) // 2 - v1)
if v4 >= v2 + 1:
    v6 = v4
else:
    v6 = v4 + v2 + 1
if v5 + v2 >= v2 + 1:
    v7 = v5 + v2
elif v5 == 0:
    v7 = v2 - 1
else:
    v7 = v5 + v2 + v2 + 1
print(min(v6, v7, v3))
