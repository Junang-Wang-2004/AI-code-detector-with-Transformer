class C1(object):

    def missingElement(self, a1, a2):
        """
        """

        def missing_count(a1, a2):
            return a1[a2] - a1[0] + 1 - (a2 - 0 + 1)

        def check(a1, a2, a3):
            return a2 > missing_count(a1, a3)
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        assert check(a1, a2, v2)
        return a1[v2] + (a2 - missing_count(a1, v2))
