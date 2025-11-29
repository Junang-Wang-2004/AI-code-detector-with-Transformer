def f1():
    v1 = input()
    if v1 == 'keyence':
        print('YES')
    else:
        for v2 in range(len(v1) - 2):
            for v3 in range(v2 + 2, len(v1) - 2):
                if v1[:v2 + 1] + v1[v3:] == 'keyence':
                    print('YES')
                    return
        for v2 in range(1, len(v1) - 5):
            for v3 in range(v2 + 3, len(v1) - 2):
                if v1[:v2] + v1[v2 + 1:v3] + v1[v3 + 1:] == 'keyence':
                    print('YES')
                    return
        print('NO')
f1()
