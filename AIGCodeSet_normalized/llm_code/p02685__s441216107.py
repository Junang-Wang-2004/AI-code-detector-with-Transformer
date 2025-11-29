def f1():
    v1 = 998244353
    v2, v3, v4 = map(int, input().split())
    v5 = v3 * pow(v3 - 1, v2 - 1, v1)
    v6 = pow(v3 - 1, v1 - 2, v1)
    v7 = v5
    v8 = 1
    for v9 in range(1, v4 + 1):
        v5 *= v6
        v5 %= v1
        v8 *= (v2 - v9 + 1) * pow(v9, v1 - 2, v1)
        v8 %= v1
        v7 += v5 * v8
        v7 %= v1
    print(v7 % v1)
if __name__ == '__main__':
    f1()
