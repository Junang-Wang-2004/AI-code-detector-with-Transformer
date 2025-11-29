class C1:

    def canFormArray(self, a1, a2):
        v1 = 0
        while v1 < len(a1):
            v2 = False
            for v3 in a2:
                v4 = len(v3)
                if v1 + v4 <= len(a1) and a1[v1:v1 + v4] == v3:
                    v1 += v4
                    v2 = True
                    break
            if not v2:
                return False
        return True
