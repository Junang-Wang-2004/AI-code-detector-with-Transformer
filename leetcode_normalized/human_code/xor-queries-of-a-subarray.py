class C1(object):

    def xorQueries(self, a1, a2):
        """
        """
        for v1 in range(1, len(a1)):
            a1[v1] ^= a1[v1 - 1]
        return [a1[right] ^ a1[left - 1] if left else a1[right] for v2, v3 in a2]
