v1 = int(input())
v2 = 10 ** 9 + 7

def f1(a1, a2, a3):
    v1 = str(format(a2, 'b'))
    v2 = 1
    for v3 in range(len(v1)):
        v2 = v2 * v2 % a3
        if v1[v3] == '1':
            v2 = v2 * a1 % a3
    return v2
v3 = f1(10, v1, v2)
v4 = f1(9, v1, v2)
v5 = f1(8, v1, v2)
print((v3 + v5 - v4 * 2 + v2) % v2)
