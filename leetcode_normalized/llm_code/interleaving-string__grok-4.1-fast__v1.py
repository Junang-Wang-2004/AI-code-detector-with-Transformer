class C1:

    def isInterleave(self, a1, a2, a3):
        if len(a1) + len(a2) != len(a3):
            return False
        v1 = {}

        def dp(a1, a2):
            if a1 == len(a1) and a2 == len(a2):
                return True
            v1 = (a1, a2)
            if v1 in v1:
                return v1[v1]
            v2 = a1 + a2
            v3 = a1 < len(a1) and a1[a1] == a3[v2] and dp(a1 + 1, a2) or (a2 < len(a2) and a2[a2] == a3[v2] and dp(a1, a2 + 1))
            v1[v1] = v3
            return v3
        return dp(0, 0)
