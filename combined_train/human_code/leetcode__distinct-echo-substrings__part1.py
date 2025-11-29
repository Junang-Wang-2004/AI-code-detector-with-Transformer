class C1(object):

    def distinctEchoSubstrings(self, a1):
        """
        """

        def KMP(a1, a2, a3):
            v1 = [-1] * (len(a1) - a2)
            v2 = -1
            for v3 in range(1, len(v1)):
                while v2 > -1 and a1[a2 + v2 + 1] != a1[a2 + v3]:
                    v2 = v1[v2]
                if a1[a2 + v2 + 1] == a1[a2 + v3]:
                    v2 += 1
                v1[v3] = v2
                if v2 + 1 and (v3 + 1) % (v3 + 1 - (v2 + 1)) == 0 and ((v3 + 1) // (v3 + 1 - (v2 + 1)) % 2 == 0):
                    a3.add(a1[a2:a2 + v3 + 1])
            return len(v1) - (v1[-1] + 1) if v1[-1] + 1 and len(v1) % (len(v1) - (v1[-1] + 1)) == 0 else float('inf')
        v1 = set()
        v2, v3 = (0, len(a1) - 1)
        while v2 < v3:
            v3 = min(v3, v2 + KMP(a1, v2, v1))
            v2 += 1
        return len(v1)
