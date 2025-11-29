class C1(object):

    def minimumTimeRequired(self, a1, a2):
        """
        """

        def backtracking(a1, a2, a3, a4):
            if a2 == len(a1):
                a4[0] = min(a4[0], max(a3))
                return
            for v1 in range(len(a3)):
                if a3[v1] + a1[a2] <= a4[0]:
                    a3[v1] += a1[a2]
                    backtracking(a1, a2 + 1, a3, a4)
                    a3[v1] -= a1[a2]
                if a3[v1] == 0:
                    break
        a1.sort(reverse=False)
        v1 = [sum(a1)]
        backtracking(a1, 0, [0] * a2, v1)
        return v1[0]
