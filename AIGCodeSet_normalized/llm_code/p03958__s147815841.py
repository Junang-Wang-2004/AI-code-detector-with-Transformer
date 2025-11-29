v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [0] * v2
for v5 in range(v2):
    v4[v5] = (v3[v5], v5)
if v2 == 1:
    print(v1 - 1)
else:
    v4.sort()
    v4[-1] = (v4[-1][0] - 1, v4[-1][1])
    v6 = v4[-1][1]
    v7 = 0
    while True:
        v4.sort()
        if v4[-1][0] == 0:
            print(v7)
            break
        elif v4[-1][1] != v6:
            v4[-1] = (v4[-1][0] - 1, v4[-1][1])
            v6 = v4[-1][1]
        elif v4[-2][0] == 0:
            print(v7 + v4[-1][0])
            break
        else:
            v4[-2] = (v4[-2][0] - 1, v4[-2][1])
            v6 = v4[-2][1]
            v7 += 1
