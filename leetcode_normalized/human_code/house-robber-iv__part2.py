class C1(object):

    def minCapability(self, a1, a2):
        """
        """

        def check(a1):
            v1 = v2 = 0
            while v2 < len(a1):
                if a1[v2] <= a1:
                    v1 += 1
                    v2 += 2
                else:
                    v2 += 1
            return v1 >= a2
        v1, v2 = (min(a1), max(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
