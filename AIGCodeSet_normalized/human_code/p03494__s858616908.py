v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(31):
    for v5 in range(v1):
        if v2[v5] % 2 == 0:
            v2[v5] = v2[v5] // 2
            v3 += 1
        else:
            break
print(v3 // v1)
