v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [1] * v1
for v5 in range(v2):
    for v6 in range(v1):
        for v7 in range(v3[v6] + 1):
            v4[v6 + v7] += 1
            if v6 - v7 >= 0:
                v4[v6 - v7] += 1
    for v6 in range(v1):
        if v5 != v2 - 1:
            v3[v6] = v4[v6]
        else:
            print(v3[v6], ' ', end='')
