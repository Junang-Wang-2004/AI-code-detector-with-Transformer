class C1(object):

    def twoSum(self, a1, a2):
        """
        """
        v1 = {}
        for v2, v3 in enumerate(a1):
            if a2 - v3 in v1:
                return [v1[a2 - v3], v2]
            v1[v3] = v2

    def twoSum2(self, a1, a2):
        """
        """
        for v1 in a1:
            v2 = a2 - v1
            v3 = a1.index(v1) + 1
            v4 = a1[v3:]
            if v2 in v4:
                return [a1.index(v1), v3 + v4.index(v2)]
