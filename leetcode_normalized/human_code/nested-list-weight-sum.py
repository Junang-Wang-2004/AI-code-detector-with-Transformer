class C1(object):

    def depthSum(self, a1):
        """
        """

        def depthSumHelper(a1, a2):
            v1 = 0
            for v2 in a1:
                if v2.isInteger():
                    v1 += v2.getInteger() * a2
                else:
                    v1 += depthSumHelper(v2.getList(), a2 + 1)
            return v1
        return depthSumHelper(a1, 1)
