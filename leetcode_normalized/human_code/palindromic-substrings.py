class C1(object):

    def countSubstrings(self, a1):
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
        return sum(((max_len + 1) // 2 for v1 in manacher(a1)))
