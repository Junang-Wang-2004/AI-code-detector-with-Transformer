class C1(object):

    def minimumRelativeLosses(self, a1, a2):
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
        a1.sort()
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = []
        for v4, v5 in a2:
            v6 = binary_search(0, v5 - 1, lambda x: v4 - (a1[-(v5 - x)] - v4) <= a1[x + 1 - 1] - 0)
            v7 = v1[-1] - v1[-1 - (v5 - v6)] - (v5 - v6) * v4
            v8 = v1[v6] + (v5 - v6) * v4
            v3.append(v8 - v7)
        return v3
