v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in v2:
    v5 = 0
    while v4 % 2 == 0:
        v4 = v4 / 2
        v5 += 1
    v3.append(v5)
print(min(v3))
