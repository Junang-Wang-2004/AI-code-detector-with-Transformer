class C1:

    def isScramble(self, a1, a2):
        if len(a1) != len(a2):
            return False
        v1 = {}

        def helper(a1, a2, a3):
            v1 = (a1, a2, a3)
            if v1 in v1:
                return v1[v1]
            if a3 == 1:
                v2 = a1[a1] == a2[a2]
            elif a1[a1:a1 + a3] == a2[a2:a2 + a3]:
                v2 = True
            else:
                v2 = False
                for v3 in range(1, a3):
                    if helper(a1, a2, v3) and helper(a1 + v3, a2 + v3, a3 - v3) or (helper(a1, a2 + a3 - v3, v3) and helper(a1 + v3, a2, a3 - v3)):
                        v2 = True
                        break
            v1[v1] = v2
            return v2
        return helper(0, 0, len(a1))
