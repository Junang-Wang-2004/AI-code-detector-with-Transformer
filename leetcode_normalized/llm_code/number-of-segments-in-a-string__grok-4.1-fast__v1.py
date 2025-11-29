class C1:

    def countSegments(self, a1):
        v1 = 0
        v2 = True
        for v3 in a1:
            if v3 != ' ':
                if v2:
                    v1 += 1
                v2 = False
            else:
                v2 = True
        return v1
