v1 = int(input())
v2 = v1 - 1
v3 = 'A' + input().replace(' ', 'A') + 'C'
v4 = [list(map(int, input().split())) for v5 in range(v2)]
v6 = [0]
v7 = 0
for v8 in range(v1):
    if v3[v8] == 'A' and v3[v8 + 1] == 'C':
        v7 += v4[v8][0]
    elif v3[v8] == 'C' and v3[v8 + 1] == 'A':
        v7 += (v4[v8 - 1][1] - 1) % v4[v8 - 1][2] + 1
    v6.append(v7)
for v8 in range(1, v1 + 1):
    print(v6[v8] - v6[0])
