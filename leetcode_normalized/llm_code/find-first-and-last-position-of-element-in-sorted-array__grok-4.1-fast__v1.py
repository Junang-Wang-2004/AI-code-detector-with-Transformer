class C1:

    def searchRange(self, a1, a2):
        v1 = len(a1)
        v2, v3 = (0, v1)
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if a1[v4] < a2:
                v2 = v4 + 1
            else:
                v3 = v4
        v5 = v2
        if v5 == v1 or a1[v5] != a2:
            return [-1, -1]
        v2, v3 = (0, v1)
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if a1[v4] <= a2:
                v2 = v4 + 1
            else:
                v3 = v4
        v6 = v2 - 1
        return [v5, v6]
