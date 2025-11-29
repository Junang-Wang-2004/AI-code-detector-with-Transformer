class C1(object):

    def sortArray(self, a1):
        """
        """

        def min_moves(a1):

            def index(a1):
                return a1 * (len(a1) - 1) if a1 == 0 else a1 - a1
            v1 = [False] * len(a1)
            v2 = len(a1)
            for v3 in range(len(a1)):
                if v1[a1[v3]]:
                    continue
                v4 = 0
                while not v1[a1[v3]]:
                    v1[a1[v3]] = True
                    v4 += 1
                    v3 = index(a1[v3])
                v2 -= 1
                if v4 >= 2:
                    v2 += 2
            return v2 - 2 * int(a1[a1 * (len(a1) - 1)] != 0)
        return min(min_moves(0), min_moves(1))
