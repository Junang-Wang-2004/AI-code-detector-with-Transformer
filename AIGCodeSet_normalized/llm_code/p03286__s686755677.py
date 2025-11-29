v1 = int(input())
v2 = bin(v1)
v3 = []

def f1(a1, a2, a3):
    v1 = a3
    if a2 == 1:
        return v1 + str(a1 % 2)
    for v2 in range(a2 - 1, -1, -1):
        if a1 >= v3[v2 - 1][0] and a1 <= v3[v2 - 1][1]:
            v1 += '1'
            return f1(a1 - (-2) ** v2, v2, v1)
        else:
            v1 += '0'
            if v2 == 0:
                return v1 + str(a1 % 2)
if v1 == 0:
    print('0')
elif v1 == 1:
    print('1')
else:
    for v4 in range(1, 30):
        v5 = sum([(-2) ** j for v6 in range(1, v4, 2)]) + (-2) ** v4
        v7 = sum([(-2) ** v6 for v6 in range(0, v4, 2)]) + (-2) ** v4
        v3.append([v5, v7])
    v8 = f1(v1, 30, '')
    print(v8.lstrip('0'))
