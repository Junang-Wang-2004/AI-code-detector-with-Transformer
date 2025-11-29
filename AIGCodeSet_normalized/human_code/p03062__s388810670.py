v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = []
for v5 in v2:
    if v5 < 0:
        v3 += 1
    v4.append(abs(v5))
if v3 % 2 == 0:
    print(sum(v4))
else:
    print(sum(v4) - 2 * min(v4))
