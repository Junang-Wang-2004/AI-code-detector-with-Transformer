def f1():
    v1, v2 = tuple((int(i) for v3 in input().split()))
    v4, v5, v6 = tuple((int(v3) for v3 in input().split()))
    v7 = input()
    v8 = {'r': v6, 's': v4, 'p': v5}
    v9 = []
    v10 = 0
    for v3 in range(v1):
        v11 = v7[v3]
        if v3 < v2:
            v9.append(v11)
            v10 += v8[v11]
        elif v9[v3 - v2] == v11:
            v9.append('x')
        else:
            v9.append(v11)
            v10 += v8[v11]
    print(v10)
if __name__ == '__main__':
    f1()
