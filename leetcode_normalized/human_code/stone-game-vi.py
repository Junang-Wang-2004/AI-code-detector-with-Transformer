class C1(object):

    def stoneGameVI(self, a1, a2):
        """
        """
        v1 = sorted(((a, b) for v2, v3 in zip(a1, a2)), key=sum, reverse=True)
        return cmp(sum((v2 for v2, v4 in v1[::2])), sum((v3 for v4, v3 in v1[1::2])))
