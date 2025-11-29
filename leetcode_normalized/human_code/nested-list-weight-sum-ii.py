class C1(object):

    def depthSumInverse(self, a1):
        """
        """

        def depthSumInverseHelper(a1, a2, a3):
            if len(a3) < a2 + 1:
                a3.append(0)
            if a1.isInteger():
                a3[a2] += a1.getInteger()
            else:
                for v1 in a1.getList():
                    depthSumInverseHelper(v1, a2 + 1, a3)
        v1 = []
        for list in a1:
            depthSumInverseHelper(list, 0, v1)
        sum = 0
        for v2 in reversed(range(len(v1))):
            sum += v1[v2] * (len(v1) - v2)
        return sum
