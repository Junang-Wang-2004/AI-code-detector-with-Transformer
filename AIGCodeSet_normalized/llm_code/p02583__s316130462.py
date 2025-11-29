v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    for v5 in range(v4 + 1, v1):
        for v6 in range(v5 + 1, v1):
            v7 = v2[v4]
            v8 = v2[v5]
            v9 = v2[v6]
            if v7 != v8 and v8 != v9 and (v9 != v7):
                if v7 + v8 > v9 and v8 + v9 > v7 and (v9 + v7 > v8):
                    v3 += 1
print(v3)
