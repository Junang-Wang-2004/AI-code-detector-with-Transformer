class C1(object):

    def checkPartitioning(self, a1):
        """
        """

        def manacher(a1):
            a1 = '^#' + '#'.join(a1) + '#$'
            v2 = [0] * len(a1)
            v3, v4 = (0, 0)
            for v5 in range(1, len(a1) - 1):
                v6 = 2 * v3 - v5
                if v4 > v5:
                    v2[v5] = min(v4 - v5, v2[v6])
                while a1[v5 + 1 + v2[v5]] == a1[v5 - 1 - v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3, v4 = (v5, v5 + v2[v5])
            return v2
        v1 = manacher(a1)
        v2, v3 = ([], [])
        for v4 in range(2, len(v1) - 2):
            if v4 - 1 - v1[v4] == 0:
                v2.append(v4)
            if v4 + 1 + v1[v4] == len(v1) - 1:
                v3.append(v4)
        for v4 in v2:
            for v5 in v3:
                v6, v7 = (v4 + 1 + v1[v4], v5 - 1 - v1[v5])
                if v6 > v7:
                    continue
                v8 = v6 + (v7 - v6) // 2
                if v1[v8] >= v8 - v6:
                    return True
        return False
