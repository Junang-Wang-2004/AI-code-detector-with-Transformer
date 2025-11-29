class C1:

    def rotateString(self, a1, a2):
        v1 = len(a1)
        if v1 != len(a2):
            return False
        for v2 in range(v1):
            v3 = True
            for v4 in range(v1):
                if a1[(v2 + v4) % v1] != a2[v4]:
                    v3 = False
                    break
            if v3:
                return True
        return False
