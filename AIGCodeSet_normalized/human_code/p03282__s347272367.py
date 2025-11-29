v1 = input()
v2 = float(input())
v3 = list(v1)
v4 = set(v3)
if len(v4) == 1:
    print(v1[0])
elif v2 <= len(v1):
    v5 = v3[:int(v2)]
    v6 = set(v5)
    if len(v6) == 1:
        print(v5[0])
    else:
        for v7 in v3:
            if int(v7) != 1:
                print(int(v7))
                break
else:
    for v7 in v3:
        if int(v7) != 1:
            print(int(v7))
            break
