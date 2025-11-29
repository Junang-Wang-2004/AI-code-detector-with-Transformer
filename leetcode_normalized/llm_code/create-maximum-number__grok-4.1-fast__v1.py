class C1:

    def maxNumber(self, a1, a2, a3):

        def pick_best(a1, a2):
            v1 = []
            v2 = len(a1) - a2
            for v3 in a1:
                while v1 and v2 and (v1[-1] < v3):
                    v1.pop()
                    v2 -= 1
                v1.append(v3)
            return v1[:a2]

        def merge_max(a1, a2):
            v1 = []
            v2 = v3 = 0
            while v2 < len(a1) and v3 < len(a2):
                if a1[v2:] > a2[v3:]:
                    v1.append(a1[v2])
                    v2 += 1
                else:
                    v1.append(a2[v3])
                    v3 += 1
            v1 += a1[v2:]
            v1 += a2[v3:]
            return v1
        v1, v2 = (len(a1), len(a2))
        v3 = []
        for v4 in range(max(0, a3 - v2), min(a3, v1) + 1):
            v5 = a3 - v4
            v6 = merge_max(pick_best(a1, v4), pick_best(a2, v5))
            if v6 > v3:
                v3 = v6
        return v3
