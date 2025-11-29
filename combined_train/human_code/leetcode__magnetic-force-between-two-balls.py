class C1(object):

    def maxDistance(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            v1, v2 = (1, a1[0])
            for v3 in range(1, len(a1)):
                if a1[v3] - v2 >= a3:
                    v1 += 1
                    v2 = a1[v3]
            return v1 >= a2
        a1.sort()
        v1, v2 = (1, a1[-1] - a1[0])
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
