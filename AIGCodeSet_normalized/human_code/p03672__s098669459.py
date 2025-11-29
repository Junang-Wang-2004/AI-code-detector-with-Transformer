v1 = list(input())
while len(v1) != 0:
    v1.pop()
    if len(v1) % 2 == 0 and v1[:len(v1) // 2] == v1[len(v1) // 2:]:
        print(len(v1))
        exit()
