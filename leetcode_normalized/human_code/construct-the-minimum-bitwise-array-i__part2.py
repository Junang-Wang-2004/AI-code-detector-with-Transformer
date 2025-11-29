class C1(object):

    def minBitwiseArray(self, a1):
        """
        """
        return [next((i for v1 in range(x) if v1 | v1 + 1 == x), -1) for v2 in a1]
