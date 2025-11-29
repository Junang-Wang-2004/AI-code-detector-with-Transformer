v1 = int(input())
v2 = list(map(int, input().split(' ')))
v3 = 0
v4 = 0
while True:
    for v5 in range(len(v2)):
        if v2[v5] % 2 == 0:
            v2[v5] = v2[v5] / 2
        else:
            v4 = -1
            break
    if v4 == -1:
        break
    v3 += 1
print(v3)
