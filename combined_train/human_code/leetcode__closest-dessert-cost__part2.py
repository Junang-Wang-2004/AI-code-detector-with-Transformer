class C1(object):

    def closestCost(self, a1, a2, a3):
        """
        """
        v1 = 2

        def backtracking(a1, a2, a3, a4, a5, a6):
            if (a2, a3) in a5:
                return
            a5.add((a2, a3))
            if a3 >= a4 or a2 == len(a1):
                if (abs(a3 - a4), a3) < (abs(a6[0] - a4), a6[0]):
                    a6[0] = a3
                return
            for v1 in range(v1 + 1):
                backtracking(a1, a2 + 1, a3 + v1 * a1[a2], a4, a5, a6)
        v2 = [float('inf')]
        v3 = set()
        for v4 in a1:
            backtracking(a2, 0, v4, a3, v3, v2)
        return v2[0]
