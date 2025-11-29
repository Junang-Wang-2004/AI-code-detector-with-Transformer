v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = sum(v2)
if v4 % 10 != 0:
    print(v4)
else:
    for v3 in range(len(v2)):
        if v2[v3] % 10 != 0:
            print(v4 - v2[v3])
            break
    else:
        print(0)
