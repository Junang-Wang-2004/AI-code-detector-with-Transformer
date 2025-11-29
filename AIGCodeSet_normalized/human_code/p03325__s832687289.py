v1 = 0
v2 = int(input())
v3 = list(map(int, input().split()))
for v4 in v3:
    while True:
        if v4 % 2 == 0:
            v1 += 1
            v4 = v4 // 2
        else:
            break
print(v1)
