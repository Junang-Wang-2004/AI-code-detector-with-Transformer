class C1:

    def maximumBobPoints(self, a1, a2):
        v1 = len(a2)
        v2 = [-1]
        v3 = [None]
        v4 = [0] * v1

        def explore(a1, a2):
            if a1 == -1:
                v4[v1 - 1] += a2
                v1 = sum((k for v2, v3 in enumerate(a2) if v4[v2] > v3))
                if v1 > v2[0]:
                    v2[0] = v1
                    v3[0] = v4[:]
                v4[v1 - 1] -= a2
                return
            v4[a1] = 0
            explore(a1 - 1, a2)
            v4 = a2[a1] + 1
            if a2 >= v4:
                v4[a1] = v4
                explore(a1 - 1, a2 - v4)
                v4[a1] = 0
        explore(v1 - 1, a1)
        return v3[0]
