def f1():
    v1, v2 = map(int, input().split())
    v3 = []
    for v4 in range(10):
        v3.append(list(map(int, input().split())))
    v5 = [j[1] for v6 in v3]
    v7 = [0 for v8 in range(10)]
    v9 = [(v6, g) for v6, v10 in enumerate(v5) if v6 != 1]
    v11 = min(v9, key=lambda a: a[1])[0]
    v7[v11] = 1
    while sum(v7) != 10:
        for v6 in range(10):
            if v3[v6][v11] + v5[v11] < v5[v6]:
                v5[v6] = v3[v6][v11] + v5[v11]
        v9 = [(k, v10) for v12, v10 in enumerate(v5) if v7[v12] == 0 and v12 != v6]
        if v9 != []:
            v11 = min(v9, key=lambda a: a[1])[0]
        else:
            break
        v7[v11] = 1
    v13 = 0
    for v4 in range(v1):
        v14 = list(map(int, input().split()))
        v13 += sum([v5[v4] for v4 in v14 if v4 != -1])
    return v13
if __name__ == '__main__':
    print(f1())
