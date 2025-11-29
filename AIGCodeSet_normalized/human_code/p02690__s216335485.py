v1 = int(input())
for v2 in range(-118, 120):
    for v3 in range(-119, 119):
        if v2 ** 5 - v3 ** 5 == v1:
            print(v2, v3)
            exit()
