def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = 1000
    for v4 in range(v1 - 1):
        v5 = 1000
        v6 = [0 for v7 in range(v1)]
        v6[v4] = 1
        v8 = v4
        for v9 in range(v4 + 1, v1):
            if v2[v9] > v2[v8]:
                v6[v9] = 1
                if v9 > 0 and v6[v9 - 1] == 1:
                    v6[v9 - 1] = 0
                v8 = v9
            elif v2[v8] > v2[v9]:
                v6[v9] = -1
                if v9 > 0 and v6[v9 - 1] == -1:
                    v6[v9 - 1] = 0
                v8 = v9
            else:
                v6[v9] = 0
                v8 = v9
        v10 = v5 // v2[v4]
        v5 = v5 - v10 * v2[v4]
        v11 = 0
        for v12 in range(len(v6)):
            if v6[v12] == 1:
                v5 = v5 + v10 * v2[v12]
                v10 = 0
            elif v6[v12] == -1:
                v10 = v5 // v2[v12]
                v5 = v5 - v10 * v2[v12]
                v11 = v12
        v5 = v5 + v10 * v2[v11]
        if v5 > v3:
            v3 = v5
    print(v3)
if __name__ == '__main__':
    f1()
