class C1(object):

    def countDistinctStrings(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        return pow(2, len(a1) - a2 + 1, v1)
