v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    v5 = 1
    while True:
        if v2[v4] % 2 ** v5:
            v3 += v5 - 1
            break
        v5 += 1
print(v3)
