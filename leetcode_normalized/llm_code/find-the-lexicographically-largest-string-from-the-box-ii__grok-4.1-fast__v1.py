class C1:

    def answerString(self, a1, a2):
        if a2 == 1:
            return a1
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = 1
        while v4 < v1:
            if a1[v4] == a1[v2 + v3]:
                v3 += 1
                v4 += 1
            elif a1[v4] < a1[v2 + v3]:
                v3 = 0
                v4 += 1
            else:
                v5 = v4 - v3
                if a1[v5] >= a1[v4]:
                    v2 = v5
                else:
                    v2 = v4
                v3 = 0
                v4 += 1
        v6 = max(a2 - 1 - v2, 0)
        return a1[v2:v1 - v6]
