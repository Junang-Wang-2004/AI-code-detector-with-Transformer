class C1(object):

    def subsequenceCount(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        return pow(2, len(a1) - 1, v1) if any((x % 2 for v2 in a1)) else 0
