class C1(object):

    def isBalanced(self, a1):
        """
        """
        return sum((ord(a1[i]) - ord('0') for v1 in range(0, len(a1), 2))) == sum((ord(a1[v1]) - ord('0') for v1 in range(1, len(a1), 2)))
