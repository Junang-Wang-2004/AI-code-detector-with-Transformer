v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = 0
for v5 in range(v1):
    for v6 in range(v5 + 1, v1):
        if v2[v5][v6] < 0 or v2[v5][v6] != v2[v6][v5]:
            print(-1)
            exit()
        for v7 in range(v1):
            if v2[v5][v7] > v2[v5][v6] + v2[v6][v7]:
                print(-1)
                exit()
        v4 += v2[v5][v6]
print(v4)
