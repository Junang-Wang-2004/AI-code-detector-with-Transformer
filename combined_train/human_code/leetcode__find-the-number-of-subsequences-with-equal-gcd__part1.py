v1 = 10 ** 9 + 7
v2 = 200

def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f2(a1, a2):
    return a1 // f1(a1, a2) * a2
v3 = [1] * (v2 + 1)
for v4 in range(len(v3) - 1):
    v3[v4 + 1] = v3[v4] * 2 % v1
v5 = [1] * (v2 + 1)
for v4 in range(len(v5) - 1):
    v5[v4 + 1] = v5[v4] * 3 % v1
v6 = [[0] * (v2 + 1) for v7 in range(v2 + 1)]
for v4 in range(1, v2 + 1):
    for v8 in range(v4, v2 + 1):
        v6[v4][v8] = v6[v8][v4] = f2(v4, v8)
v9 = [0] * (v2 + 1)
v9[1] = 1
for v4 in range(1, v2 + 1):
    for v8 in range(v4 + v4, v2 + 1, v4):
        v9[v8] -= v9[v4]

class C1(object):

    def subsequencePairCount(self, a1):
        """
        """

        def count(a1):
            return reduce(lambda accu, x: (accu + x) % v1, (v9[v4] * v9[v8] * f[v4 * a1][v8 * a1] for v4 in range(1, mx // a1 + 1) for v8 in range(1, mx // a1 + 1)), 0)
        v1 = max(a1)
        v2 = [0] * (v1 + 1)
        for v3 in a1:
            v2[v3] += 1
        for v4 in range(1, v1 + 1):
            for v5 in range(v4 + v4, v1 + 1, v4):
                v2[v4] += v2[v5]
        v6 = [[0] * (v1 + 1) for v7 in range(v1 + 1)]
        for v7 in range(1, v1 + 1):
            for v8 in range(v7, v1 + 1):
                v9 = v6[v7][v8]
                v10 = v2[v9] if v9 < len(v2) else 0
                v11, v12 = (v2[v7], v2[v8])
                v6[v7][v8] = v6[v8][v7] = (v5[v10] * v3[v11 - v10 + (v12 - v10)] - v3[v11] - v3[v12] + 1) % v1
        return reduce(lambda accu, x: (accu + v3) % v1, (count(g) for v13 in range(1, v1 + 1)), 0)
