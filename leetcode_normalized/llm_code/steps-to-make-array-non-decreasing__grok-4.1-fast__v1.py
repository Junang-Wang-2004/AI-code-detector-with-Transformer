class C1(object):

    def totalSteps(self, a1):
        v1 = []
        v2 = 0
        v3 = [0] * len(a1)
        for v4, v5 in enumerate(a1):
            v6 = 0
            while v1 and v1[-1][0] <= v5:
                v7, v8 = v1.pop()
                v6 = max(v6, v8)
            v3[v4] = v6 + 1 if v1 else 0
            v1.append((v5, v3[v4]))
            v2 = max(v2, v3[v4])
        return v2
