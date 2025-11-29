def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = [input() for v5 in range(v1)]
    v6 = 1 << 100
    for v7 in range(1 << v1 - 1):
        v8 = bin(v7).count('1')
        v9 = v8 + 1
        v10 = [0] * v9
        v11 = 1
        for v12 in range(v2):
            v13 = 0
            for v14 in range(v1):
                v10[v13] += v4[v14][v12] == '1'
                if v10[v13] > v3:
                    break
                v13 += v7 >> v14 & 1
            else:
                continue
            v10 = [0] * v9
            v8 += 1
            if v8 > v6:
                v11 = 0
                break
            v13 = 0
            for v14 in range(v1):
                v10[v13] += v4[v14][v12] == '1'
                if v10[v13] > v3:
                    break
                v13 += v7 >> v14 & 1
            else:
                continue
            v11 = 0
            break
        if v11:
            v6 = min(v6, v8)
    print(v6)
if __name__ == '__main__':
    f1()
