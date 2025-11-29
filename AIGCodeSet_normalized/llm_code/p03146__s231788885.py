def f1(a1):
    if a1 % 2 == 0:
        return a1 // 2
    else:
        return a1 * 3 + 1
v1 = 0
v2 = 1
v3 = int(input())
while True:
    v2 += 1
    v3 = f1(v3)
    if v3 == 4:
        if v1 == 0:
            v1 = 1
        else:
            print(v2 - 1)
            break
