v1 = 10 ** 9 + 7
v2 = int(input())
v3 = 'ATCG'
v4 = {}

def f1(a1, a2):
    if a1 == v2:
        return 1
    v1 = (a1, a2)
    if v1 in v4:
        return v4[v1]
    v2 = None
    v3 = a2[-2:]
    if v3 == 'AC':
        v2 = 'G'
    elif v3 == 'AG':
        v2 = 'C'
    elif v3 == 'GA':
        v2 = 'C'
    elif a2 == 'AGG' or a2 == 'ATG' or a2 == 'AGT':
        v2 = 'C'
    v4 = 0
    for v5 in v3:
        if v5 == v2:
            continue
        v4 += f1(a1 + 1, a2[1:] + v5)
    v4[v1] = v4 = v4 % v1
    return v4
print(f1(0, '***'))
