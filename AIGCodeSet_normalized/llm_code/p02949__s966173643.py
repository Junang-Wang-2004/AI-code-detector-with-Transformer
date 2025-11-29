v1 = pow(10, 15)

def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = []
    for v5 in range(v2):
        v6, v7, v8 = map(int, input().split())
        v4.append((v6 - 1, v7 - 1, v8))
    v9 = [v1 for v5 in range(v1)]
    v10 = [-1 for v5 in range(v1)]
    v9[0] = 0
    for v5 in range(v1):
        for v11 in v4:
            if v9[v11[0]] == v1:
                continue
            if v9[v11[1]] > v9[v11[0]] + v11[2]:
                v9[v11[1]] = v9[v11[0]] + v11[2]
                v10[v11[1]] = v11[0]
    v12 = {}
    v13 = v1 - 1
    while v10[v13] != -1:
        if v13 in v12:
            break
        v12[v13] = v10[v13]
        v13 = v10[v13]
    v14 = False
    for v11 in v4:
        if v9[v11[1]] > v9[v11[0]] + v11[2]:
            if v11[0] in v12:
                v14 = True
                break
    if v14:
        print(-1)
    elif v9[-1] == v1:
        print(-1)
    else:
        print(v9[-1])
if __name__ == '__main__':
    f1()
