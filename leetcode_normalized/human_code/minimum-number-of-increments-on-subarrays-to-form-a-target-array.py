class C1(object):

    def minNumberOperations(self, a1):
        """
        """
        return sum((max((a1[i] if i < len(a1) else 0) - (a1[i - 1] if i - 1 >= 0 else 0), 0) for v1 in range(len(a1) + 1)))
