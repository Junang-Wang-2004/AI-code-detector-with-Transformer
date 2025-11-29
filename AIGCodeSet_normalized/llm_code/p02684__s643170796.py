v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [0] * v1
v5, v6 = ([], [])
v7 = 0
while v4[v7] < 2:
    if v4[v7]:
        v6.append(v3[v7])
        v2 -= 1
    else:
        v5.append(v3[v7])
        v2 += 1
    v4[v7] += 1
    v7 = v3[v7] - 1
print(v6[v2 % len(v6) - 1])
