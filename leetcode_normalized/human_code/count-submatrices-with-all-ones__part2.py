class C1(object):

    def numSubmat(self, a1):
        """
        """

        def count(a1):
            v1, v2 = ([0] * len(a1), [])
            for v3 in range(len(a1)):
                while v2 and a1[v2[-1]] >= a1[v3]:
                    v2.pop()
                v1[v3] = v1[v2[-1]] + a1[v3] * (v3 - v2[-1]) if v2 else a1[v3] * (v3 - -1)
                v2.append(v3)
            return sum(v1)
        v1 = 0
        v2 = [0] * len(a1[0])
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v2[v4] = v2[v4] + 1 if a1[v3][v4] == 1 else 0
            v1 += count(v2)
        return v1
