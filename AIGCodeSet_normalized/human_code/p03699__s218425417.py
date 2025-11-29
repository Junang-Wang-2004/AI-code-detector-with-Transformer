v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v2 = sorted(v2)
if sum(v2) % 10 != 0:
    print(sum(v2))
else:
    for v3 in range(v1):
        if (sum(v2) - v2[v3]) % 10 != 0:
            print(sum(v2) - v2[v3])
            exit()
    else:
        print('0')
