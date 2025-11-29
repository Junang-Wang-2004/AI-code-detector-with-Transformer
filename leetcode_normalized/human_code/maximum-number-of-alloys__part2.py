class C1(object):

    def maxNumberOfAlloys(self, a1, a2, a3, a4, a5, a6):
        """
        """

        def check(a1):
            for v1 in a4:
                v2 = 0
                for v3 in range(a1):
                    v2 += max(a1 * v1[v3] - a5[v3], 0) * a6[v3]
                    if v2 > a3:
                        break
                if v2 <= a3:
                    return True
            return False
        v1, v2 = (1, min(a5) + a3)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
