class C1(object):

    def minDeletionSize(self, a1):
        """
        """
        v1 = [1] * len(a1[0])
        for v2 in range(1, len(a1[0])):
            for v3 in range(v2):
                if all((a1[k][v3] <= a1[k][v2] for v4 in range(len(a1)))):
                    v1[v2] = max(v1[v2], v1[v3] + 1)
        return len(a1[0]) - max(v1)
