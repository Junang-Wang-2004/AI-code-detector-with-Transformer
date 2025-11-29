class C1(object):

    def minSteps(self, a1):
        v1 = [0] * (a1 + 1)
        for v2 in range(2, a1 + 1):
            v1[v2] = v2
            for v3 in range(2, int(v2 ** 0.5) + 1):
                if v2 % v3 == 0:
                    v1[v2] = min(v1[v2], v1[v3] + v2 // v3)
                    v1[v2] = min(v1[v2], v1[v2 // v3] + v3)
        return v1[a1]
