v1 = int(input())
v2 = list(map(int, input().split()))
v2.append(0)
v3 = 0
v4 = 1000
v5 = 0
v6 = 0
while v6 < v1:
    if v3 == 0:
        if v2[v6] < v2[v6 + 1]:
            v5 = v4 // v2[v6]
            v4 = v4 % v2[v6]
            v3 = 1
            v6 += 1
        else:
            v6 += 1
    elif v2[v6] > v2[v6 + 1]:
        v4 += v2[v6] * v5
        v5 = 0
        v3 = 0
        v6 += 1
    else:
        v6 += 1
print(v4)
