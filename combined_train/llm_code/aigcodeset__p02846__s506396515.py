def f1():
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    v3 = list(map(int, input().split()))
    v4 = v2[0] * v1[0]
    v5 = v2[1] * v1[1]
    v6 = v3[0] * v1[0]
    v7 = v3[1] * v1[1]
    v8 = v4 + v5
    v9 = v6 + v7
    if v8 == v9:
        return 'infinity'
    v10 = v4 - v6
    v11 = v5 - v7
    v12 = v8 - v9
    if v10 * v11 > 0:
        return 0
    v13 = v12 + v10
    v14 = v12 + v11
    if v10 * v12 < 0:
        return -v13 // v12 + 1
    else:
        return -v14 // v12 + 1
if __name__ == '__main__':
    print(f1())
