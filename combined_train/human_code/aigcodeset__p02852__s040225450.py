v1, v2 = map(int, input().split())
v3 = input()
v3 = v3[::-1]
v4 = 0
v5 = 1
v6 = []
while True:
    for v7 in range(min(v2, v1 - v4), 0, -1):
        if v3[v4 + v7] == '0':
            v4 += v7
            v6.append(str(v7))
            break
        if v7 == 1:
            print(-1)
            v5 = 0
            break
    if v5 == 0:
        break
    if v4 == v1:
        break
if v5 == 1:
    print(' '.join(v6[::-1]))
