class C1:

    def canSeePersonsCount(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = []
        for v4 in range(v1 - 1, -1, -1):
            v5 = 0
            while v3 and a1[v3[-1]] < a1[v4]:
                v3.pop()
                v5 += 1
            if v3:
                v5 += 1
            v2[v4] = v5
            if v3 and a1[v3[-1]] == a1[v4]:
                v3.pop()
            v3.append(v4)
        return v2
