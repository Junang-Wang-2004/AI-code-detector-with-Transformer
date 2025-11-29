class C1(object):

    def colorTheArray(self, a1, a2):
        """
        """

        def update(a1):
            if not nums[a1]:
                return 0
            v1 = 0
            if a1 - 1 >= 0 and nums[a1 - 1] == nums[a1]:
                v1 += 1
            if a1 + 1 < a1 and nums[a1 + 1] == nums[a1]:
                v1 += 1
            return v1
        v1 = [0] * a1
        v2 = [0] * len(a2)
        v3 = 0
        for v4, (v5, v6) in enumerate(a2):
            v3 -= update(v5)
            v1[v5] = v6
            v3 += update(v5)
            v2[v4] = v3
        return v2
