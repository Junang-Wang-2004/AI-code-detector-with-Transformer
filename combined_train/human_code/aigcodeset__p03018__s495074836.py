def f1():
    v1 = input()
    v2 = 0
    v3 = 0
    v4 = 0
    v2 = 0
    for v5 in range(len(v1)):
        if v4 == 0:
            if v1[v5] == 'A':
                v3 = 1
                v4 = 1
            else:
                v3 = 0
        elif v4 == 1:
            if v1[v5] == 'B':
                v4 = 2
            elif v1[v5] == 'A':
                v3 += 1
            else:
                v3 = 0
                v4 = 0
        elif v4 == 2:
            if v1[v5] == 'C':
                v2 += v3
                v4 = 1
            elif v1[v5] == 'A':
                v3 = 1
                v4 = 1
            else:
                v4 = 0
                v3 = 0
    print(v2)
f1()
