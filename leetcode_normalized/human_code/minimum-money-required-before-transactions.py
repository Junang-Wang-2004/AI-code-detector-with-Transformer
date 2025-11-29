class C1(object):

    def minimumMoney(self, a1):
        """
        """
        return sum((max(a - b, 0) for v1, v2 in a1)) + max((v1 - max(v1 - v2, 0) for v1, v2 in a1))
