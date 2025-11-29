v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = 0
if v2[0] != 0:
    print(-1)
    exit()
for v5 in range(v1 - 1):
    if v2[v5 + 1] - v2[v5] > 1:
        print(-1)
        exit()
    elif v2[v5] + 1 == v2[v5 + 1]:
        v4 += 1
    else:
        v4 += v2[v5 + 1]
print(v4)
