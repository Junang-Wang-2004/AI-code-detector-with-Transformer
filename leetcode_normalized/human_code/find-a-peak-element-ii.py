class C1(object):

    def findPeakGrid(self, a1):
        """
        """

        def get_vec(a1, a2):
            return a1[a2] if len(a1) > len(a1[0]) else (a1[j][a2] for v1 in range(len(a1)))

        def check(a1, a2):
            return max(get_vec(a1, a2)) > max(get_vec(a1, a2 + 1))
        v1, v2 = (0, max(len(a1), len(a1[0])) - 1 - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(a1, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        v4 = max(get_vec(a1, v1))
        v5 = [v1, next((i for v6, v7 in enumerate(get_vec(a1, v1)) if v7 == v4))]
        return v5 if len(a1) > len(a1[0]) else v5[::-1]
