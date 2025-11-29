class C1(object):

    def maxDivScore(self, a1, a2):
        """
        """
        return max(a2, key=lambda d: (sum((x % d == 0 for v1 in a1)), -d))
