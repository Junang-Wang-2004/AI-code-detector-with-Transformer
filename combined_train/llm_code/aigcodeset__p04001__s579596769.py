def f1(a1, a2):
    v1 = bin(a1)[2:]
    while a2 > len(v1):
        v1 = '0' + v1
    v1 = v1 + '1'
    return v1

def f2(a1, a2):
    v1 = ''
    v2 = 0
    for v3 in range(len(a1)):
        v1 = v1 + a1[v3]
        if a2[v3] == '1':
            v2 = v2 + int(v1)
            v1 = ''
    v2 = v2 + int(v1)
    return v2
v1 = input()
v2 = len(v1)
v3 = 0
for v4 in range(2 ** (v2 - 1)):
    v5 = f1(v4, v2 - 1)
    v3 = v3 + f2(v1, v5)
print(v3)
