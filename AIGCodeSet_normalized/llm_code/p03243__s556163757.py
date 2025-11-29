v1 = int(input())
if v1 % 111 == 0:
    print(v1)
else:
    for v2 in range(10):
        if v1 // 111 == v2:
            print(111 * (v2 + 1))
