class C1(object):

    def maxJump(self, a1):
        """
        """
        return a1[1] - a1[0] if len(a1) == 2 else max((a1[i + 2] - a1[i] for v1 in range(len(a1) - 2)))
