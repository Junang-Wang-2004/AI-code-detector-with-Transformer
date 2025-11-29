class C1(object):

    def numJewelsInStones(self, a1, a2):
        """
        """
        v1 = set(a1)
        return sum((s in v1 for v2 in a2))
