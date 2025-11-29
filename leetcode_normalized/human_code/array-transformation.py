class C1(object):

    def transformArray(self, a1):
        """
        """

        def is_changable(a1):
            return any((a1[i - 1] > a1[i] < a1[i + 1] or a1[i - 1] < a1[i] > a1[i + 1] for v1 in range(1, len(a1) - 1)))
        while is_changable(a1):
            v1 = a1[:]
            for v2 in range(1, len(a1) - 1):
                v1[v2] += a1[v2 - 1] > a1[v2] < a1[v2 + 1]
                v1[v2] -= a1[v2 - 1] < a1[v2] > a1[v2 + 1]
            a1 = v1
        return a1
