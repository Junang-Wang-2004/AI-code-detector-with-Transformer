def f1(a1):
    return bin(a1).count('1')
v1 = 10 ** 15
v2 = v1.bit_length()
v3 = [[0] * (v2 + 1) for v4 in range(v2 + 1)]
for v5 in range(v2 + 1):
    for v6 in range(v5 + 1):
        v3[v5][v6] = v3[v5 - 1][v6] + v3[v5 - 1][v6 - 1] if 0 < v6 < v5 else 1
v7 = [0] * (v2 + 1)
for v5 in range(2, v2 + 1):
    v7[v5] = v7[f1(v5)] + 1

class C1(object):

    def popcountDepth(self, a1, a2):
        """
        """

        def count(a1):
            v1 = v2 = 0
            for v3 in reversed(range(a1.bit_length())):
                if not a1 & 1 << v3:
                    continue
                if 0 <= a1 - v2 <= v3:
                    v1 += v3[v3][a1 - v2]
                v2 += 1
            if v2 == a1:
                v1 += 1
            return v1
        if a2 == 0:
            return 1
        if a2 == 1:
            return a1.bit_length() - 1
        return sum((count(c) for v1 in range(2, a1.bit_length() + 1) if v7[v1] == a2 - 1))
