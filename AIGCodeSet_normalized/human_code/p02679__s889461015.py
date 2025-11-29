v1 = 1000000007
v2 = 10 ** (-9)

def f1():
    import sys
    from math import gcd
    input = sys.stdin.buffer.readline
    v1 = int(input())
    v2 = {}
    v3 = 0
    for v4 in range(v1):
        v5, v6 = map(int, input().split())
        if v5 == v6 == 0:
            v3 += 1
            continue
        if v5 < 0:
            v5 = -v5
            v6 = -v6
        elif v5 == 0:
            if v6 < 0:
                v6 = -v6
        v7 = gcd(abs(v5), abs(v6))
        v8 = (v5 // v7, v6 // v7)
        if v8 in v2:
            v2[v8] += 1
        else:
            v2[v8] = 1
    v9 = 1
    v10 = 0
    for v8 in v2:
        if v2[v8] == 0:
            continue
        v5, v6 = v8
        if v6 > 0:
            v11 = (v6, -v5)
        else:
            v11 = (-v6, v5)
        if v11 in v2:
            v12 = v2[v8]
            v13 = v2[v11]
            v2[v11] = 0
            v9 = v9 * (pow(2, v12, v1) - 1 + (pow(2, v13, v1) - 1) + 1) % v1 % v1
        else:
            v10 += v2[v8]
    v9 = v9 * pow(2, v10, v1) % v1
    v9 = (v9 - 1) % v1
    print((v9 + v3) % v1)
if __name__ == '__main__':
    f1()
