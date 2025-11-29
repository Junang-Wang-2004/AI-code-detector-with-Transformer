class C1:

    def numSubmat(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [0] * v2
        v4 = 0

        def calc_mins(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3 = []
            for v4 in range(v1):
                while v3 and a1[v3[-1]] >= a1[v4]:
                    v3.pop()
                v5 = v3[-1] if v3 else -1
                v2[v4] = (v2[v5] if v5 >= 0 else 0) + a1[v4] * (v4 - v5)
                v3.append(v4)
            return sum(v2)
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] == 1:
                    v3[v6] += 1
                else:
                    v3[v6] = 0
            v4 += calc_mins(v3)
        return v4
