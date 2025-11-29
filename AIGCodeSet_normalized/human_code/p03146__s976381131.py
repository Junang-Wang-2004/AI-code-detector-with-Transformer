v1 = int(input())
v2 = []
v3 = 2
while True:
    v2.append(v1)
    if v1 % 2 == 0:
        v1 = v1 // 2
    else:
        v1 = 3 * v1 + 1
    if v1 in v2:
        print(v3)
        exit()
    v3 += 1
