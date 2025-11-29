class C1(object):

    def combinationSum4(self, a1, a2):
        """
        """
        v1 = [0] * (a2 + 1)
        v1[0] = 1
        a1.sort()
        for v2 in range(1, a2 + 1):
            for v3 in range(len(a1)):
                if a1[v3] <= v2:
                    v1[v2] += v1[v2 - a1[v3]]
                else:
                    break
        return v1[a2]
