class C1(object):

    def lexSmallest(self, a1):
        """
        """
        return min((min(a1[:k][::-1] + a1[k:], a1[:-k] + a1[-k:][::-1]) for v1 in range(1, len(a1) + 1)))
