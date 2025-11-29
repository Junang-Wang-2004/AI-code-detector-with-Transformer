def f1(a1, a2):
    v1, v2 = (1, 1)
    for v3, v4 in a2:
        v5 = v3 * v2 % v4
        v6 = max(0, (v1 * v4 - v3 * v2) // v3)
        while True:
            if (v5 + v6 * v3) % v4 == 0:
                break
            v6 += 1
        v7 = (v3 * v2 + v3 * v6) // v4 - v1
        v1 += v7
        v2 += v6
    return v1 + v2
if __name__ == '__main__':
    v1 = int(input())
    v2 = [tuple(map(int, input().split(' '))) for v3 in range(v1)]
    print(f1(v1, v2))
