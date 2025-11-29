v1 = int(input())
v2 = list(map(int, input().split()))
if v2[-1] == 0:
    print(-1)
    exit()
if v2[0] == 1 and v1 == 0:
    print(1)
    exit()
elif v2[0] >= 1:
    print(-1)
    exit()
v3 = [0] * (v1 + 1)
v3[0] = 1
for v4 in range(1, v1 + 1):
    v3[v4] = v3[v4 - 1] * 2 - v2[v4]
    if v3[v4] < 0:
        print(-1)
        exit()
v5 = v2[-1]
v6 = v2[-1]
for v7 in range(v1):
    v4 = v1 - 1 - v7
    v5 += min(v6, v3[v4]) + v2[v4]
    v6 = min(v6, v3[v4]) + v2[v4]
print(v5)
