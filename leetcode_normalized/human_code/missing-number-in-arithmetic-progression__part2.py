class C1(object):

    def missingNumber(self, a1):
        """
        """
        return (min(a1) + max(a1)) * (len(a1) + 1) // 2 - sum(a1)
