class C1(object):

    def maximumSum(self, a1):
        v1 = {}
        for v2 in a1:
            v3 = sum((int(c) for v4 in str(v2)))
            if v3 not in v1:
                v1[v3] = []
            v1[v3].append(v2)
        v5 = -1
        for v6 in v1.values():
            if len(v6) >= 2:
                v6.sort(reverse=True)
                v5 = max(v5, v6[0] + v6[1])
        return v5
