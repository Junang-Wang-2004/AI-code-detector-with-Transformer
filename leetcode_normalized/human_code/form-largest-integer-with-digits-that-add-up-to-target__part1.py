class C1(object):

    def largestNumber(self, a1, a2):
        """
        """
        v1 = [0]
        for v2 in range(1, a2 + 1):
            v1.append(-1)
            for v3, v4 in enumerate(a1):
                if v2 - v4 < 0 or v1[v2 - v4] < 0:
                    continue
                v1[v2] = max(v1[v2], v1[v2 - v4] + 1)
        if v1[a2] < 0:
            return '0'
        v5 = []
        for v3 in reversed(range(9)):
            while a2 >= a1[v3] and v1[a2] == v1[a2 - a1[v3]] + 1:
                a2 -= a1[v3]
                v5.append(v3 + 1)
        return ''.join(map(str, v5))
