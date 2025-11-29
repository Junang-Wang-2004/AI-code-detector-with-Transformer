v1 = 10 ** 9 + 7

def f1():
    v1, v2 = map(int, input().split())
    v3 = sorted(map(int, input().split()))
    v4 = [1]
    for v5 in range(1, v1 + 1):
        v4.append(v4[-1] * v5 % v1)
    v6 = [1]
    for v5 in range(1, v1 + 1):
        v6.append(pow(v4[v5], v1 - 2, v1))

    def nCr(a1, a2):
        return v4[a1] * v6[a2] * v6[a1 - a2] % v1
    v7 = 0
    for v5 in range(v2 - 1, v1):
        v7 += v3[v5] * nCr(v5, v2 - 1)
        v7 -= v3[v5 - v2 + 1] * nCr(v5 + 1, v2)
        v7 %= v1
    print(v7)
if __name__ == '__main__':
    f1()
