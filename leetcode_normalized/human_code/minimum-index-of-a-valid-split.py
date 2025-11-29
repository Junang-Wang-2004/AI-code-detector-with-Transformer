class C1(object):

    def minimumIndex(self, a1):
        """
        """

        def boyer_moore_majority_vote():
            v1, v2 = (None, 0)
            for v3 in a1:
                if not v2:
                    v1 = v3
                if v3 == v1:
                    v2 += 1
                else:
                    v2 -= 1
            return v1
        v1 = boyer_moore_majority_vote()
        v2, v3 = (a1.count(v1), 0)
        for v4, v5 in enumerate(a1):
            if v5 == v1:
                v3 += 1
            if v3 * 2 > v4 + 1 and (v2 - v3) * 2 > len(a1) - (v4 + 1):
                return v4
        return -1
