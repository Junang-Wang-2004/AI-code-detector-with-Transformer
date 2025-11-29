class C1:

    def minimumTime(self, a1, a2):
        a1 = sorted(a1)
        a2 = sorted(a2)
        v3 = min(a1[0], a2[0])
        v4 = max(a1[-1], a2[-1])

        def can_cover(a1):
            v1 = 0
            v2 = len(a2)
            for v3 in a1:
                if v1 >= v2:
                    return True
                v4 = v3 - a2[v1]
                if v4 > a1:
                    return False
                if v4 <= 0:
                    v5 = a1
                else:
                    v6 = v4
                    v7 = a1 - 2 * v6
                    v8 = (a1 - v6) // 2
                    v5 = max(v7, v8)
                v9 = v3 + v5
                while v1 < v2 and a2[v1] <= v9:
                    v1 += 1
                if v1 >= v2:
                    return True
            return v1 >= v2
        v5 = 0
        v6 = 2 * (v4 - v3)
        while v5 < v6:
            v7 = (v5 + v6) // 2
            if can_cover(v7):
                v6 = v7
            else:
                v5 = v7 + 1
        return v5
