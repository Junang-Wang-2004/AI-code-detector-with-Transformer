from decimal import *
v1 = 1000000007

def f1(a1, a2):
    v1 = {}
    v2 = 10 ** 18
    v3 = 0
    for v4, v5 in a2:
        if v4 == 0 and v5 == 0:
            v3 += 1
            continue
        if v5 == 0:
            v6 = 'INF'
        else:
            v6 = Decimal(v4) / Decimal(v5)
        v1.setdefault(v6, 0)
        v1[v6] += 1
    v7 = set()
    v8 = []
    for v6, v9 in v1.items():
        if v6 in v7:
            continue
        v10 = 0
        v10 += pow(2, v9, v1)
        if v6 == 'INF':
            v11 = 0
        elif v6 == 0:
            v11 = 'INF'
        else:
            v11 = -(Decimal(1) / Decimal(v6))
        if v11 in v1.keys():
            v10 += pow(2, v1[v11], v1)
            v7.add(v11)
            v10 -= 1
        v8.append(v10 % v1)
    v12 = 1
    for v10 in v8:
        v12 *= v10
        v12 %= v1
    if v3:
        v12 += v3
        v12 %= v1
    return (v12 - 1) % v1
if __name__ == '__main__':
    v2 = int(input())
    v3 = [tuple(map(int, input().split(' '))) for v4 in range(v2)]
    print(f1(v2, v3))
