def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = []
    v4 = 0
    v5 = []
    v3 = v2[0]
    v6 = v2[0]
    for v7 in range(v1):
        while True:
            if v4 == v1 - 1:
                v5.append((v7, v4))
                break
            else:
                v8 = v3 ^ v2[v4 + 1]
                v9 = v3 + v2[v4 + 1]
                if v8 != v9:
                    v5.append((v7, v4))
                    v3 ^= v2[v7]
                    v6 -= v2[v7]
                    if v7 == v4:
                        v4 += 1
                    break
                else:
                    v4 += 1
                    v3 = v8
                    v6 = v9
    v10 = 0
    for v7 in v5:
        v10 += v7[1] - v7[0] + 1
    print(v10)
if __name__ == '__main__':
    f1()
