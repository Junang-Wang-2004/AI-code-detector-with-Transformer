class C1(object):

    def countBits(self, a1):
        """
        """
        v1 = [0]
        for v2 in range(1, a1 + 1):
            v1.append((v2 & 1) + v1[v2 >> 1])
        return v1

    def countBits2(self, a1):
        """
        """
        v1 = [0]
        while len(v1) <= a1:
            v1.extend([x + 1 for v2 in v1])
        return v1[:a1 + 1]
