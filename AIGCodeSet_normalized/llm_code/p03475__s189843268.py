v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(list(map(int, input().split())))
    if v3 == v1 - 2:
        break
for v3 in range(v1 - 1):
    if v3 == v1 - 1:
        break
    sum = v2[v3][0] + v2[v3][1]
    for v4 in range(v3 + 1, v1 - 1):
        if v2[v4][1] > sum:
            sum = v2[v4][1] + v2[v4][0]
            break
        v5 = sum - v2[v4][1]
        if not (sum - v2[v4][1]) % v2[v4][2] == 0:
            if v5 < v2[v4][2]:
                sum += v2[v4][2] - v5
            elif v5 > v2[v4][2]:
                sum += v2[v4][2] - v5 % v2[v4][2]
        sum += v2[v4][0]
    print(sum)
print(0)
