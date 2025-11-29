v1 = input()
while True:
    v1 = v1[0:-1]
    v2 = v1[0:len(v1) // 2]
    if v1 == v2 * 2:
        print(len(v1))
        exit()
