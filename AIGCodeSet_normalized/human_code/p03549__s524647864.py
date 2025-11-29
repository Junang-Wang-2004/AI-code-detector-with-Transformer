def f1():
    v1, v2 = (int(i) for v3 in input().split())
    v4 = 0.5 ** v2
    v5 = 1 - v4
    v6 = 1900 * v2 + 100 * (v1 - v2)
    v7 = 0
    for v3 in range(1, 10 ** 5)[::-1]:
        v7 += v3 * v6 * v4 * v5 ** (v3 - 1)
    print(round(v7))
if __name__ == '__main__':
    f1()
