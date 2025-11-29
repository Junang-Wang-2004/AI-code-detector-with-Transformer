class C1(object):

    def fillCups(self, a1):
        """
        """
        return max(max(a1), (sum(a1) + 1) // 2)
