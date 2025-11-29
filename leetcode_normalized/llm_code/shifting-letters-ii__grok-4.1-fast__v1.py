class C1(object):

    def shiftingLetters(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3, v4, v5 in a2:
            v6 = 2 * v5 - 1
            v2[v3] += v6
            if v4 + 1 <= v1:
                v2[v4 + 1] -= v6
        v7 = []
        v8 = 0
        v9 = ord('a')
        for v10 in range(v1):
            v8 += v2[v10]
            v11 = (ord(a1[v10]) - v9 + v8) % 26
            v7.append(chr(v9 + v11))
        return ''.join(v7)
