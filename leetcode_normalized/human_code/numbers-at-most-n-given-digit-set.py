class C1(object):

    def atMostNGivenDigitSet(self, a1, a2):
        """
        """
        v1 = str(a2)
        v2 = set(a1)
        v3 = sum((len(a1) ** i for v4 in range(1, len(v1))))
        v4 = 0
        while v4 < len(v1):
            v3 += sum((c < v1[v4] for v5 in a1)) * len(a1) ** (len(v1) - v4 - 1)
            if v1[v4] not in v2:
                break
            v4 += 1
        return v3 + int(v4 == len(v1))
