class C1(object):

    def minimizeMax(self, a1, a2):
        """
        """

        def check(a1):
            v1 = v2 = 0
            while v1 + 1 < len(a1) and v2 < a2:
                if a1[v1 + 1] - a1[v1] <= a1:
                    v1 += 1
                    v2 += 1
                v1 += 1
            return v2 == a2
        a1.sort()
        v1, v2 = (0, a1[-1] - a1[0])
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
