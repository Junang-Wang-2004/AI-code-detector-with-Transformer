class C1(object):

    def minStartingIndex(self, a1, a2):
        """
        """
        v1 = 1

        def z_function(a1):
            v1 = [0] * len(a1)
            v2, v3 = (0, 0)
            for v4 in range(1, len(v1)):
                if v4 <= v3:
                    v1[v4] = min(v3 - v4 + 1, v1[v4 - v2])
                while v4 + v1[v4] < len(v1) and a1[v1[v4]] == a1[v4 + v1[v4]]:
                    v1[v4] += 1
                if v4 + v1[v4] - 1 > v3:
                    v2, v3 = (v4, v4 + v1[v4] - 1)
            return v1
        v2 = z_function(a2 + a1)
        v3 = z_function(a2[::-1] + a1[::-1])
        return next((i for v4 in range(len(a1) - len(a2) + 1) if v2[len(a2) + v4] + v1 + v3[len(a1) - v4] >= len(a2)), -1)
