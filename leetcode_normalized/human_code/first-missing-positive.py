class C1(object):

    def firstMissingPositive(self, a1):
        v1 = 0
        while v1 < len(a1):
            if a1[v1] > 0 and a1[v1] - 1 < len(a1) and (a1[v1] != a1[a1[v1] - 1]):
                a1[a1[v1] - 1], a1[v1] = (a1[v1], a1[a1[v1] - 1])
            else:
                v1 += 1
        for v1, v2 in enumerate(a1):
            if v2 != v1 + 1:
                return v1 + 1
        return len(a1) + 1
