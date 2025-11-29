class C1(object):

    def findMaximumElegance(self, a1, a2):
        """
        """
        a1.sort(reverse=True)
        v1 = v2 = 0
        v3 = set()
        v4 = []
        for v5 in range(a2):
            if a1[v5][1] in v3:
                v4.append(a1[v5][0])
            v2 += a1[v5][0]
            v3.add(a1[v5][1])
        v1 = v2 + len(v3) ** 2
        for v5 in range(a2, len(a1)):
            if a1[v5][1] in v3:
                continue
            if not v4:
                break
            v2 += a1[v5][0] - v4.pop()
            v3.add(a1[v5][1])
            v1 = max(v1, v2 + len(v3) ** 2)
        return v1
