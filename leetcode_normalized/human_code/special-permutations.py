class C1(object):

    def specialPerm(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def backtracking(a1, a2):
            if a2 == (1 << len(a1)) - 1:
                return 1
            if lookup[a1 + 1][a2] == -1:
                v1 = 0
                for v2 in range(len(a1)):
                    if a2 & 1 << v2:
                        continue
                    if not (a1 == -1 or a1[a1] % a1[v2] == 0 or a1[v2] % a1[a1] == 0):
                        continue
                    v1 = (v1 + backtracking(v2, a2 | 1 << v2)) % v1
                lookup[a1 + 1][a2] = v1
            return lookup[a1 + 1][a2]
        v2 = [[-1] * (1 << len(a1)) for v3 in range(len(a1) + 1)]
        return backtracking(-1, 0)
