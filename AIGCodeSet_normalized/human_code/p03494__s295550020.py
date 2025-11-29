v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
while True:
    v4 = False
    for v5 in range(v1):
        if v2[v5] % 2 == 0:
            v2[v5] = v2[v5] / 2
            continue
        else:
            v4 = True
            break
    if v4:
        break
    v3 += 1
print(v3)
