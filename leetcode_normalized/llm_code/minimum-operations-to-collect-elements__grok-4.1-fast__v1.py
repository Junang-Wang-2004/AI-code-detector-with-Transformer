class C1(object):

    def minOperations(self, a1, a2):
        v1 = set()
        v2 = len(a1)
        for v3 in range(v2 - 1, -1, -1):
            if a1[v3] <= a2:
                v1.add(a1[v3])
            if len(v1) == a2:
                return v2 - v3
        return v2
