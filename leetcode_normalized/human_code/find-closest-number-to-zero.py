class C1(object):

    def findClosestNumber(self, a1):
        """
        """
        return max(a1, key=lambda x: (-abs(x), x))
