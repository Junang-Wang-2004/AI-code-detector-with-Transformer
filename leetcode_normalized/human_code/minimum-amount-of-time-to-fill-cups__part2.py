class C1(object):

    def fillCups(self, a1):
        """
        """
        v1, v2 = (max(a1), sum(a1))
        return v1 if sum(a1) - v1 <= v1 else (v2 + 1) // 2
