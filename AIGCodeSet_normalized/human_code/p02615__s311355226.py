v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort(reverse=True)
v3 = 0
v4 = v1 - 1
for v5, v6 in enumerate(v2):
    v7 = 2
    if v5 == 0:
        v7 = 1
    for v8 in range(v7):
        if v4 > 0:
            v3 += v6
        v4 -= 1
print(v3)
