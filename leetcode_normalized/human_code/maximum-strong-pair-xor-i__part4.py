class C1(object):

    def maximumStrongPairXor(self, a1):
        """
        """
        return max((a1[i] ^ a1[j] for v1 in range(len(a1)) for v2 in range(v1, len(a1)) if abs(a1[v1] - a1[v2]) <= min(a1[v1], a1[v2])))
