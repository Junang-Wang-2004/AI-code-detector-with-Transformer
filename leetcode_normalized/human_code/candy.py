class C1(object):

    def candy(self, a1):
        v1 = [1 for v2 in range(len(a1))]
        for v3 in range(1, len(a1)):
            if a1[v3] > a1[v3 - 1]:
                v1[v3] = v1[v3 - 1] + 1
        for v3 in reversed(range(1, len(a1))):
            if a1[v3 - 1] > a1[v3] and v1[v3 - 1] <= v1[v3]:
                v1[v3 - 1] = v1[v3] + 1
        return sum(v1)
