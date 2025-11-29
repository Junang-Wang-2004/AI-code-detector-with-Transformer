class C1(object):

    def earliestSecondToMarkIndices(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = sum(a1) + v1

        def feasible(a1):
            v1 = [-1] * v1
            for v2 in range(a1):
                v1[a2[v2] - 1] = v2
            if -1 in v1:
                return False
            v3 = 0
            for v2 in range(a1):
                v4 = a2[v2] - 1
                if v2 == v1[v4]:
                    v3 -= a1[v4]
                else:
                    v3 += 1
                if v3 < 0:
                    return False
            return True
        v4, v5 = (v3, v2)
        while v4 <= v5:
            v6 = v4 + (v5 - v4) // 2
            if feasible(v6):
                v5 = v6 - 1
            else:
                v4 = v6 + 1
        return v4 if v4 <= v2 else -1
