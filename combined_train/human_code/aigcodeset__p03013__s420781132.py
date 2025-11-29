import sys
v1, v2 = list(map(int, input().split()))
if v2 == 0:
    v3 = []
else:
    v3 = sys.stdin.readlines()
    v3 = set(map(int, list(set(v3))))
if v1 == 1:
    print(1)
elif v1 == 2:
    if v2 == 1:
        print(1)
    else:
        print(2)
else:
    v4 = []
    v4.append(1)
    if 1 in v3:
        v4.append(-1)
    else:
        v4.append(1)
    for v5 in range(2, v1 + 1):
        if v4[v5 - 2] < 0 and v4[v5 - 1] < 0:
            print(0)
            exit()
        v4.append(0)
        if v5 in v3:
            v4[v5] = -1
        else:
            if v4[v5 - 1] >= 0:
                v4[v5] += v4[v5 - 1]
            if v4[v5 - 2] >= 0:
                v4[v5] += v4[v5 - 2]
            v4[v5] = v4[v5] % 1000000007
    print(int(v4[v1]))
