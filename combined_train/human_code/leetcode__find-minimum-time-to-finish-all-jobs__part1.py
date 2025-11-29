class C1(object):

    def minimumTimeRequired(self, a1, a2):
        """
        """

        def backtracking(a1, a2, a3, a4):
            if a2 == len(a1):
                return True
            for v1 in range(len(a4)):
                if a4[v1] + a1[a2] <= a3:
                    a4[v1] += a1[a2]
                    if backtracking(a1, a2 + 1, a3, a4):
                        return True
                    a4[v1] -= a1[a2]
                if a4[v1] == 0:
                    break
            return False
        a1.sort(reverse=True)
        v1, v2 = (max(a1), sum(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if backtracking(a1, 0, v3, [0] * a2):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
