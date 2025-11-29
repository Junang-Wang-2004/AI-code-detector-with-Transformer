class C1(object):

    def subsequenceCount(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * 2
        for v3 in a1:
            v2 = [(v2[i] + v2[i ^ v3 % 2] + int(v3 % 2 == i)) % v1 for v4 in range(2)]
        return v2[1]
