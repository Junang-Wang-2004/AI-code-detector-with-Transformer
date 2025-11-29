class C1(object):

    def maximizeSweetness(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            v1, v2 = (0, 0)
            for v3 in a1:
                v1 += v3
                if v1 >= a3:
                    v2 += 1
                    v1 = 0
            return v2 >= a2 + 1
        v1, v2 = (min(a1), sum(a1) // (a2 + 1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
