def f1():
    v1, v2 = map(int, input().split())
    v3 = [list(map(int, input().split())) for v4 in range(v1)]
    v5 = []
    for v6 in range(1, v1 + 1):
        for v7 in range(1, v2 + 1):
            if v6 == v1 and v7 == v2:
                break
            if v7 == v2:
                v8, v9 = (v6 + 1, v7)
            else:
                v8, v9 = (v6, v7 + 1)
            if v3[v6 - 1][v7 - 1] % 2 == 1:
                v3[v6 - 1][v7 - 1] -= 1
                v3[v8 - 1][v9 - 1] += 1
                v5.append((v6, v7, v8, v9))
    print(len(v5))
    for v6, v7, v8, v9 in v5:
        print(v6, v7, v8, v9)
if __name__ == '__main__':
    f1()
