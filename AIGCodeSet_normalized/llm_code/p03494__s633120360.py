v1 = 0
v2 = False
v3 = list(map(int, input().split()))
while True:
    v4 = []
    for v5 in v3:
        if v5 % 2 == 0:
            v4.append(v5 // 2)
        else:
            print(v1)
            v2 = True
            break
    if v2:
        break
    v3 = v4
    v1 += 1
