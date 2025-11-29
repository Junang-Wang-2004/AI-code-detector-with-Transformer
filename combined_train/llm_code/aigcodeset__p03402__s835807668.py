def f1(a1, a2):
    if a1 > a2:
        return a2
    else:
        return a1

def f2(a1, a2):
    v1 = a2
    for v2 in range(0, 49):
        if v1 <= 0:
            break
        elif v2 % 2 == 0:
            for v3 in range(0, f1(50, v1) * 2):
                if v3 % 2 == 0:
                    a1[v2][v3] = '.'
            v1 -= 50
    return a1

def f3(a1, a2):
    v1 = a2
    for v2 in range(51, 100):
        if v1 <= 0:
            break
        elif v2 % 2 == 0:
            for v3 in range(0, f1(50, v1) * 2):
                if v3 % 2 == 0:
                    a1[v2][v3] = '#'
            v1 -= 50
    return a1
v1 = input().split()
v2 = int(v1[0])
v3 = int(v1[1])
v4 = []
v5 = []
for v6 in range(0, 100):
    v4.append('#')
    v5.append('.')
v7 = []
for v6 in range(0, 50):
    v7.append(v4)
for v6 in range(50, 100):
    v7.append(v5)
v7 = f2(v7, v2)
v7 = f3(v7, v3)
print('100 100')
for v6 in range(0, 100):
    for v8 in range(0, 99):
        print(v7[v6][v8], end='')
    print(v7[v6][99])
