class C1(object):

    def validSequence(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        v3 = [-1] * v2
        v4 = v2 - 1
        for v5 in range(v1 - 1, -1, -1):
            if v4 >= 0 and a1[v5] == a2[v4]:
                v3[v4] = v5
                v4 -= 1
        v6 = []
        v7 = 0
        for v8 in range(v1):
            if len(v6) == v2:
                break
            v9 = len(v6)
            v10 = a1[v8] == a2[v9]
            v11 = v7 == 0 and (v9 == v2 - 1 or v3[v9 + 1] > v8)
            if v10 or v11:
                if not v10:
                    v7 += 1
                v6.append(v8)
        return v6 if len(v6) == v2 else []
