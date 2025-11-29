v1 = int(input())
v2 = 10 ** 9 + 7
v3 = [{} for v4 in range(v1 + 1)]

def f1(a1):
    for v1 in range(4):
        v2 = list(a1)
        if v1 > 0:
            v2[v1], v2[v1 - 1] = (v2[v1 - 1], v2[v1])
        if ''.join(v2).count('AGC') >= 1:
            return False
    return True

def f2(a1, a2):
    if a2 in v3[a1]:
        return v3[a1][a2]
    if a1 >= v1:
        return 1
    v1 = 0
    for v2 in list('ACGT'):
        v3 = a2 + v2
        if f1(v3):
            v1 += f2(a1 + 1, v3[1:])
        v3[a1][a2] = v1
    return v1 % v2
print(f2(0, 'TTT'))
