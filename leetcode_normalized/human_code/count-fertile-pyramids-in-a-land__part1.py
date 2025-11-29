class C1(object):

    def countPyramids(self, a1):
        """
        """

        def count(a1, a2):

            def get_grid(a1, a2):
                return a1[~a1][a2] if a2 else a1[a1][a2]
            v1 = 0
            v2 = [0] * len(a1[0])
            for v3 in range(1, len(a1)):
                v4 = [0] * len(a1[0])
                for v5 in range(1, len(a1[0]) - 1):
                    if get_grid(v3, v5) == get_grid(v3 - 1, v5 - 1) == get_grid(v3 - 1, v5) == get_grid(v3 - 1, v5 + 1) == 1:
                        v4[v5] = min(v2[v5 - 1], v2[v5 + 1]) + 1
                v2 = v4
                v1 += sum(v2)
            return v1
        return count(a1, False) + count(a1, True)
