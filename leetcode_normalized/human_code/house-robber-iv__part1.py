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
        v1 = sorted(set(a1))
        v2, v3 = (0, len(v1) - 1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(v1[v4]):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v1[v2]
