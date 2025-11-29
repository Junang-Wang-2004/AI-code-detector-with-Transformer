class C1(object):

    def shiftingLetters(self, a1, a2):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2, v3, v4 in a2:
            v1[v2] += 1 if v4 else -1
            v1[v3 + 1] -= 1 if v4 else -1
        v5 = []
        v6 = 0
        for v7 in range(len(a1)):
            v6 += v1[v7]
            v5.append(chr(ord('a') + (ord(a1[v7]) - ord('a') + v6) % 26))
        return ''.join(v5)
