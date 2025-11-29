def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = 10 ** 10
    v5 = [v4] * v1
    v3 = (v3 + 1) // 2
    for v6 in range(v2 + 1):
        if v6 % 2 == 0:
            v5[v6] = v3
        else:
            v5[v6] = v3 - 1
    print(' '.join(map(str, v5)))
if __name__ == '__main__':
    f1()
