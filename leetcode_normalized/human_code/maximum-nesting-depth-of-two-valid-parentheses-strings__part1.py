class C1(object):

    def maxDepthAfterSplit(self, a1):
        """
        """
        return [i & 1 ^ (a1[i] == '(') for v1, v2 in enumerate(a1)]
