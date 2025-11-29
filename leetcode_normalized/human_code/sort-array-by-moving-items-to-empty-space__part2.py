class C1(object):

    def sortArray(self, a1):
        """
        """

        def min_moves(a1):

            def index(a1):
                return a1 * (len(a1) - 1) if a1 == 0 else a1 - a1
            v1 = a1[:]
            v2 = 0
            for v3 in range(len(v1)):
                v4, v5 = (1, v1[v3] == 0)
                while index(v1[v3]) != v3:
                    v6 = index(v1[v3])
                    v1[v3], v1[v6] = (v1[v6], v1[v3])
                    v4 += 1
                    v5 |= v1[v3] == 0
                if v4 >= 2:
                    v2 += v4 - 1 if v5 else v4 + 1
            return v2
        return min(min_moves(0), min_moves(1))
