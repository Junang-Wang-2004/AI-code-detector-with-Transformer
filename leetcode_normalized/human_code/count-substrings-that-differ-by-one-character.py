class C1(object):

    def countSubstrings(self, a1, a2):
        """
        """

        def count(a1, a2):
            v1 = v2 = v3 = 0
            for v4 in range(min(len(a1) - a1, len(a2) - a2)):
                v3 += 1
                if a1[a1 + v4] != a2[a2 + v4]:
                    v2, v3 = (v3, 0)
                v1 += v2
            return v1
        return sum((count(i, 0) for v1 in range(len(a1)))) + sum((count(0, j) for v2 in range(1, len(a2))))
