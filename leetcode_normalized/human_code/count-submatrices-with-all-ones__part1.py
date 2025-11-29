class C1(object):

    def numSubmat(self, a1):
        """
        """

        def count(a1):
            v1 = v2 = 0
            v3 = []
            for v4 in range(len(a1)):
                while v3 and a1[v3[-1]] >= a1[v4]:
                    v5 = v3.pop()
                    v2 -= (a1[v5] - a1[v4]) * (v5 - (v3[-1] if v3 else -1))
                v3.append(v4)
                v2 += a1[v4]
                v1 += v2
            return v1
        v1 = 0
        v2 = [0] * len(a1[0])
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v2[v4] = v2[v4] + 1 if a1[v3][v4] == 1 else 0
            v1 += count(v2)
        return v1
