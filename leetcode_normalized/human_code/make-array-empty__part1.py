class C1(object):

    def countOperationsToEmptyArray(self, a1):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x])
        return len(v1) + sum((len(v1) - (i + 1) for v2 in range(len(v1) - 1) if v1[v2] > v1[v2 + 1]))
