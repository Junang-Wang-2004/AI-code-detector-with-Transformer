class C1(object):

    def minOperations(self, a1):
        """
        """
        return max(((26 - (ord(x) - ord('a'))) % 26 for v1 in a1))
