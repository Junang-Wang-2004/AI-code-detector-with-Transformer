class C1:

    def maxTaskAssign(self, a1, a2, a3, a4):
        a1.sort()
        a2.sort()

        def feasible(a1):
            if a1 == 0:
                return True
            v1 = a3
            v2 = a1 - 1
            v3 = len(a2) - a1
            v4 = v3
            while v2 >= 0:
                v5 = a1[v2]
                while v4 < len(a2) and a2[v4] < v5:
                    v4 += 1
                if v4 < len(a2):
                    v4 += 1
                    v2 -= 1
                    continue
                if v1 <= 0:
                    return False
                v6 = v5 - a4
                while v4 < len(a2) and a2[v4] < v6:
                    v4 += 1
                if v4 < len(a2):
                    v4 += 1
                    v1 -= 1
                    v2 -= 1
                    continue
                return False
            return True
        v1, v2 = (0, min(len(a1), len(a2)))
        while v1 < v2:
            v3 = (v1 + v2 + 1) // 2
            if feasible(v3):
                v1 = v3
            else:
                v2 = v3 - 1
        return v1
