import collections

class C1(object):

    def isSolvable(self, a1, a2):
        """
        """

        def backtracking(a1, a2, a3, a4, a5, a6, a7):
            if a4 == len(a2):
                return a5 == 0
            if a3 != len(a1):
                if a4 >= len(a1[a3]) or a1[a3][a4] in a6:
                    return backtracking(a1, a2, a3 + 1, a4, a5, a6, a7)
                for v1 in range(10):
                    if v1 in a7 or (v1 == 0 and a4 == len(a1[a3]) - 1):
                        continue
                    a6[a1[a3][a4]] = v1
                    a7.add(v1)
                    if backtracking(a1, a2, a3 + 1, a4, a5, a6, a7):
                        return True
                    a7.remove(v1)
                    del a6[a1[a3][a4]]
                return False
            a5, v1 = divmod(a5 + sum((a6[w[a4]] for v3 in a1 if a4 < len(v3))), 10)
            if a2[a4] in a6:
                return v1 == a6[a2[a4]] and backtracking(a1, a2, 0, a4 + 1, a5, a6, a7)
            if v1 in a7 or (v1 == 0 and a4 == len(a2) - 1):
                return False
            a6[a2[a4]] = v1
            a7.add(v1)
            if backtracking(a1, a2, 0, a4 + 1, a5, a6, a7):
                return True
            a7.remove(v1)
            del a6[a2[a4]]
            return False
        return backtracking([w[::-1] for v1 in a1], a2[::-1], 0, 0, 0, {}, set())
