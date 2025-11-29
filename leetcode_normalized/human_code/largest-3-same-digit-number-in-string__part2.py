class C1(object):

    def largestGoodInteger(self, a1):
        """
        """
        return max((a1[i] if a1[i] == a1[i + 1] == a1[i + 2] else '' for v1 in range(len(a1) - 2))) * 3
