v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = 0
v4 = False
for v5 in v2:
    if v5 < 0:
        v3 += 1
    elif v5 == 0:
        v4 = True
v6 = list(map(abs, v2))
v6.sort()
if v4:
    print(sum(v6))
elif v3 % 2 == 0:
    print(sum(v6))
else:
    print(sum(v6) - 2 * v6[0])
