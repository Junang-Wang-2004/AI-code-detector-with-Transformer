v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
if v1 == 0:
    if v2[0] != 1:
        print(-1)
        quit()
    else:
        print(1)
        quit()
elif v2[0] > 0:
    print(-1)
    quit()
v4 = [[0, 0] for v5 in range(v1 + 1)]
v4[0] = [0, 1]
for v6 in range(1, v1 + 1):
    if v3 == 0:
        print(-1)
        quit()
    v3 = v4[v6 - 1][1] * 2
    if v3 > 10 ** 15:
        v3 = 10 ** 15
    v4[v6][0] = v2[v6]
    v4[v6][1] = v3 - v2[v6]
    if v3 - v2[v6] < 0:
        print(-1)
        quit()
v7 = [[v2[v6], 0] for v6 in range(v1 + 1)]
for v6 in range(v1 - 1, -1, -1):
    if v7[v6 + 1][0] + v7[v6 + 1][1] > v4[v6][1] * 2:
        print(-1)
        quit()
    else:
        v7[v6][1] = min(v4[v6][1], v7[v6 + 1][0] + v7[v6 + 1][1])
v3 = 0
for v6 in range(v1 + 1):
    v3 += sum(v7[v6])
print(v3)
