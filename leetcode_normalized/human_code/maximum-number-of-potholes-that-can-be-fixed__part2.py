class C1(object):

    def maxPotholes(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        for v3 in range(len(a1)):
            v2 += 1
            if v3 + 1 == len(a1) or a1[v3 + 1] != a1[v3]:
                if a1[v3] == 'x':
                    v1.append(v2)
                v2 = 0
        v1.sort()
        v4 = 0
        for v2 in reversed(v1):
            v5 = min(v2 + 1, a2)
            if v5 - 1 <= 0:
                break
            v4 += v5 - 1
            a2 -= v5
        return v4
