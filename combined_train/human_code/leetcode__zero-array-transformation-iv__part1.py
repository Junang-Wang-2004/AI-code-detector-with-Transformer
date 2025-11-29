class C1(object):

    def minZeroArray(self, a1, a2):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):

            def valid(a1, a2):
                v1 = [False] * (a2 + 1)
                v1[0] = 1
                for v2 in range(len(a1)):
                    v1 = [v1[j] or (j - a1[v2] >= 0 and v1[j - a1[v2]]) for v3 in range(a2 + 1)]
                return v1[a2]
            return all((valid([a2[j][2] for v1 in range(a1) if a2[v1][0] <= i <= a2[v1][1]], a1[i]) for v2 in range(len(a1))))
        v1 = binary_search(0, len(a2), check)
        return v1 if v1 <= len(a2) else -1
