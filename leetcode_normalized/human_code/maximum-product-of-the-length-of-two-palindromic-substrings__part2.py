class C1(object):

    def maxProduct(self, a1):
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
        import operator

        def accumulate(a1, a2=operator.add, a3=None):
            v1 = iter(a1)
            v2 = a3
            if a3 is None:
                try:
                    v2 = next(v1)
                except StopIteration:
                    return
            yield v2
            for v3 in v1:
                v2 = a2(v2, v3)
                yield v2

        def fin_max_len(a1):
            v1 = manacher(a1)
            v2 = [[(i - 2) // 2 - v1[i] // 2, (i - 2) // 2 + v1[i] // 2] for v3 in range(2, len(v1) - 2, 2)]
            v4 = [0] * len(a1)
            for v5, v6 in reversed(v2):
                v4[v6] = v6 - v5 + 1
            for v3 in reversed(range(len(a1) - 1)):
                v4[v3] = max(v4[v3], v4[v3 + 1] - 2)
            return list(accumulate(v4, max, 0))
        v1, v2 = (fin_max_len(a1), fin_max_len(a1[::-1])[::-1])
        return max((x * y for v3, v4 in zip(v1, v2)))
