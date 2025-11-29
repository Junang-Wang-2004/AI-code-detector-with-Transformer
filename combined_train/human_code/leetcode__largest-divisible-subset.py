class C1(object):

    def largestDivisibleSubset(self, a1):
        """
        """
        if not a1:
            return []
        a1.sort()
        v1 = [1] * len(a1)
        v2 = [-1] * len(a1)
        v3 = 0
        for v4 in range(len(a1)):
            for v5 in range(v4):
                if a1[v4] % a1[v5] == 0:
                    if v1[v4] < v1[v5] + 1:
                        v1[v4] = v1[v5] + 1
                        v2[v4] = v5
            if v1[v3] < v1[v4]:
                v3 = v4
        v6 = []
        v4 = v3
        while v4 != -1:
            v6.append(a1[v4])
            v4 = v2[v4]
        return v6[::-1]
