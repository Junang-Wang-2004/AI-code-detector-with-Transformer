class C1:

    def getWinner(self, a1, a2):
        if len(a1) < 2:
            return a1[0] if a1 else 0
        v1 = a1[0]
        v2 = 0
        v3 = 1
        while v3 < len(a1):
            if a1[v3] > v1:
                v1 = a1[v3]
                v2 = 1
            else:
                v2 += 1
            if v2 == a2:
                return v1
            v3 += 1
        return v1
