class C1:

    def answerString(self, a1, a2):
        if a2 == 1:
            return a1
        v1 = len(a1)
        v2 = v1 - a2 + 1
        v3 = a1[:v2]
        for v4 in range(1, v1):
            v5 = min(v2, v1 - v4)
            v6 = a1[v4:v4 + v5]
            if v6 > v3:
                v3 = v6
        return v3
