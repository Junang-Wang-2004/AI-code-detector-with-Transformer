class C1:

    def minimizeMax(self, a1, a2):
        a1.sort()
        v1, v2 = (0, a1[-1] - a1[0])

        def feasible(a1):
            v1 = 0
            v2 = 0
            v3 = len(a1)
            while v2 < v3 - 1 and v1 < a2:
                if a1[v2 + 1] - a1[v2] <= a1:
                    v1 += 1
                    v2 += 2
                else:
                    v2 += 1
            return v1 >= a2
        while v1 <= v2:
            v3 = (v1 + v2) // 2
            if feasible(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
