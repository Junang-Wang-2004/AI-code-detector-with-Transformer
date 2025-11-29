import math
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v2[0]
v4 = []
for v5 in v2[1:]:
    v3 = math.gcd(v3, v5)
    v4.append(v5)
if v3 == 1:
    v6 = [math.gcd(v4[i], v4[j]) for v7 in range(len(v4)) for v8 in range(v7 + 1, len(v4))]
    if all(v6 == [1]):
        print('pairwise coprime')
    else:
        print('setwise coprime')
else:
    print('not coprime')
