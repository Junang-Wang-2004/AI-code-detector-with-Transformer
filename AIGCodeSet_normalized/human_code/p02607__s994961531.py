v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
v4 = 0
for v5 in v2:
    if v3 % 2 != 0:
        if v5 % 2 != 0:
            v4 += 1
    v3 += 1
print(v4)
