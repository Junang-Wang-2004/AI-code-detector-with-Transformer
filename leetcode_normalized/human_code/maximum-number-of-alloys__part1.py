class C1(object):

    def maxNumberOfAlloys(self, a1, a2, a3, a4, a5, a6):
        """
        """

        def count(a1, a2):

            def cnt(a1):
                return a5[a1] // a1[a1]
            v1 = list(range(a1))
            v1.sort(key=cnt)
            v2 = cnt(v1[0])
            v3 = v4 = v5 = 0
            for v6 in range(a1):
                v4 += a6[v1[v6]] * a1[v1[v6]]
                v5 += a6[v1[v6]] * (a5[v1[v6]] % a1[v1[v6]])
                if v6 + 1 != a1 and cnt(v1[v6 + 1]) - cnt(v1[v6]) == 0:
                    continue
                v3 += v4
                a2 += v5
                v4 = v5 = 0
                v8 = min(cnt(v1[v6 + 1]) - cnt(v1[v6]) if v6 + 1 < a1 else float('inf'), a2 // v3)
                if v8 == 0:
                    break
                a2 -= v3 * v8
                v2 += v8
            return v2
        return max((count(machine, a3) for v1 in a4))
