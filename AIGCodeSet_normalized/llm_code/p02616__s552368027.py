from functools import reduce
from operator import mul
v1 = 10 ** 9 + 7
v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
if v2 == v3:
    print(reduce(mul, v4) % v1)
else:
    v5 = []
    v6 = []
    for v7 in v4:
        if v7 < 0:
            v6.append(v7)
        else:
            v5.append(v7)
    if len(v5) == 0 and v3 % 2 != 0:
        v6.sort(reverse=True)
        v6 = v6[:v3]
        print(reduce(mul, v6) % v1)
    else:
        v5.sort(reverse=True)
        v6.sort()
        v8 = 1
        v9 = 0
        v10 = 0
        v11 = 0
        while True:
            if v3 - v11 == 1:
                v8 *= v5[v9]
                print(v8 % v1)
                break
            elif 2 <= len(v6) - v10 and 2 <= len(v5) - v9:
                if v5[v9] * v5[v9 + 1] >= v6[v10] * v6[v10 + 1]:
                    v8 *= v5[v9] * v5[v9 + 1] % v1
                    v9 += 2
                    v11 += 2
                else:
                    v8 *= v6[v10] * v6[v10 + 1] % v1
                    v10 += 2
                    v11 += 2
            elif 1 >= len(v5) - v9 and 2 <= len(v6) - v10:
                v8 *= v6[v10] * v6[v10 + 1] % v1
                v10 += 2
                v11 += 2
            elif 2 <= len(v5) - v9 and 1 >= len(v6) - v10:
                v8 *= v5[v9] * v5[v9 + 1] % v1
                v9 += 2
                v11 += 2
            elif len(v5) - v9 == 1 and len(v6) - v10 == 1:
                v8 *= v5[v9] * v6[v10] % v1
                print(v8 % v1)
                break
            if v11 == v3:
                print(v8 % v1)
                break
