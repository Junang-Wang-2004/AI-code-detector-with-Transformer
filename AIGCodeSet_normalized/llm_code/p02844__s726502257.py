v1 = int(input())
v2 = input()
v3 = [[[False] * 1001] * 4] * 30001
v3[0][0][0] = True
for v4 in range(v1):
    for v5 in range(4):
        for v6 in range(1000):
            if v3[v4][v5][v6] == False:
                continue
            v3[v4 + 1][v5][v6] = True
            if v5 <= 2:
                v3[v4 + 1][v5 + 1][v6 * 10 + (ord(v2[v4]) - ord('0'))] = True
v7 = 0
for v8 in range(1000):
    if v3[v1][3][v8] == True:
        v7 += 1
print(v7)
