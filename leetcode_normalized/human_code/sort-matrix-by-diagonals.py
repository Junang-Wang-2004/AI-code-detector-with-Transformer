class C1(object):

    def sortMatrix(self, a1):
        """
        """
        v1 = [[] for v2 in range(len(a1) - 1 + (len(a1[0]) - 1) - (0 - (len(a1[0]) - 1)) + 1)]
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v1[v3 - v4].append(a1[v3][v4])
        for v3 in range(0 - (len(a1[0]) - 1), len(a1) - 1 + (len(a1[0]) - 1) + 1):
            if v3 < 0:
                v1[v3].sort(reverse=True)
            else:
                v1[v3].sort()
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                a1[v3][v4] = v1[v3 - v4].pop()
        return a1
