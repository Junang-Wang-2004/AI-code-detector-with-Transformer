class C1(object):

    def equalCountSubstrings(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(1, min(len(set(a1)), len(a1) // a2) + 1):
            v3, v4 = (collections.Counter(), 0)
            for v5, v6 in enumerate(a1):
                v3[v6] += 1
                v4 += v3[v6] == a2
                if v5 >= a2 * v2:
                    v4 -= v3[a1[v5 - a2 * v2]] == a2
                    v3[a1[v5 - a2 * v2]] -= 1
                v1 += v4 == v2
        return v1
