v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sorted(list(map(abs, v2)))
v4 = 1
for v5 in v2:
    if v5 == 0:
        print(sum(v3))
        exit(0)
    if v5 < 0:
        v4 *= -1
if v4 == 1:
    print(sum(v3))
else:
    print(sum(v3) - 2 * v3[0])
