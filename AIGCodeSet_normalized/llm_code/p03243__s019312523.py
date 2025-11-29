v1 = int(input())
for v2 in range(1000):
    v3 = str(v2)
    if len(v3) == 1 and v1 <= int(v3):
        print(int(v3))
        exit()
    elif len(v3) > 1 and all((v3[j] == v3[0] for v4 in range(1, len(v3)))):
        if v1 <= int(v3):
            print(int(v3))
            exit()
