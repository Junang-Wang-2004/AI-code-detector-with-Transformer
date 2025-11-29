class C1(object):

    def maximumLengthOfRanges(self, a1):
        v1 = len(a1)
        v2 = [-1] * v1
        v3 = []
        for v4 in range(v1):
            while v3 and a1[v3[-1]] < a1[v4]:
                v3.pop()
            if v3:
                v2[v4] = v3[-1]
            v3.append(v4)
        v5 = [v1] * v1
        v3 = []
        for v4 in range(v1 - 1, -1, -1):
            while v3 and a1[v3[-1]] <= a1[v4]:
                v3.pop()
            if v3:
                v5[v4] = v3[-1]
            v3.append(v4)
        return [v5[v4] - v2[v4] - 1 for v4 in range(v1)]
