def f1(a1, a2):
    if a2 == '0':
        return a1
    elif a2 == '1':
        if a1 == '1':
            return '0'
        else:
            return '1'

def f2(a1, a2):
    v1 = bin(a1)[2:]
    v2 = bin(a2)[2:]
    if a1 < a2:
        v1 = v1.zfill(len(v2))
    else:
        v2 = v2.zfill(len(v1))
    v3 = [f1(b1, b2) for v4, v5 in zip(v1, v2)]
    v3 = ''.join(v3)
    return int(v3, 2)
v1 = int(input())
v2 = [int(x) for v3 in input().split()]
v4 = list(set(v2))
v5 = len(v2)
if v5 < 3:
    print('Yes')
else:
    v6 = v2.count(v4[0])
    v7 = v2.count(v4[1])
    v8 = v2.count(v4[2])
    if v2[0] == f2(v2[-1], v2[1]) and v2[-1] == f2(v2[-2], v2[0]) and (v6 == v7 and v7 == v8):
        print('Yes')
    else:
        print('No')
