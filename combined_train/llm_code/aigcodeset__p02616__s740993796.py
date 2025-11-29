def f1(a1, a2, a3):
    a1.sort()
    v1 = 1
    if a1[a2 - 1] == 0 and a3 & 1:
        return 0
    if a1[a2 - 1] <= 0 and a3 & 1:
        for v2 in range(a2 - 1, a2 - a3 + 1, -1):
            v1 *= a1[v2]
        return v1
    v2 = 0
    v3 = a2 - 1
    if a3 & 1:
        v1 *= a1[v3]
        v3 -= 1
        a3 -= 1
    a3 >>= 1
    for v5 in range(a3):
        v6 = a1[v2] * a1[v2 + 1]
        v7 = a1[v3] * a1[v3 - 1]
        if v6 > v7:
            v1 *= v6
            v2 += 2
        else:
            v1 *= v7
            v3 -= 2
    return v1
if __name__ == '__main__':
    v1 = 10 ** 9 + 7
    v2, v3 = map(int, input().split())
    v4 = [int(x) for v5 in input().split()]
    print(f1(v4, v2, v3) % v1)
