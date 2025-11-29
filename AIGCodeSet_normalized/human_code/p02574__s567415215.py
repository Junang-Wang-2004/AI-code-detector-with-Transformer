v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * (10 ** 6 + 1)
for v4 in v2:
    v3[v4] += 1
v5 = 0
for v4 in range(2, 10 ** 6 + 1):
    v6 = sum(v3[v4::v4])
    if v6 == v1:
        print('not coprime')
        exit()
    elif v6 > 1:
        v5 += 1
if v5 > 0:
    print('setwise coprime')
else:
    print('pairwise coprime')
