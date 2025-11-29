import copy

def f1(a1):
    v1 = ['A', 'C', 'G', 'T']
    v2 = []
    for v3 in range(4):
        v4 = a1 // 4 ** (3 - v3)
        a1 = a1 % 4 ** (3 - v3)
        v6 = v1[v4]
        v2.append(v6)

    def acgt_sw(a1, a2, a3):
        v1 = copy.deepcopy(a1)
        v1[a2], v1[a3] = (v1[a3], v1[a2])
        return ''.join(v1)
    v7 = [''.join(v2)] + [acgt_sw(v2, v3, v3 + 1) for v3 in range(3)]
    v8 = False
    for v3 in v7:
        if v3[:3] == 'AGC':
            v8 = True
        if v3[1:] == 'AGC':
            v8 = True
    return (v8, ''.join(v2))
v1 = 10 ** 9 + 7
v2 = []
for v3 in range(256):
    if f1(v3)[0]:
        v2.append(v3)
v4 = int(input())
if v4 == 3:
    v5 = 61
else:
    v6 = [1 for v3 in range(4 ** 4)]
    for v3 in v2:
        v6[v3] = 0
    for v3 in range(v4 - 4):
        v7 = [0 for v3 in range(4 ** 4)]
        for v8 in range(4 ** 4):
            v9 = v6[v8]
            v10 = [4 * (v8 % 64) + k for v11 in range(4)]
            for v11 in v10:
                v7[v11] += v9
        for v8 in v2:
            v7[v8] = 0
            v6 = [v3 % v1 for v3 in v7]
    v5 = sum(v6) % v1
print(v5)
