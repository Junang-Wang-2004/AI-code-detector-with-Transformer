class C1(object):

    def getLeastFrequentDigit(self, a1):
        """
        """
        v1 = [0] * 10
        while a1:
            a1, v3 = divmod(a1, 10)
            v1[v3] += 1
        v4 = min((x for v5 in v1 if v5))
        return next((i for v6 in range(len(v1)) if v1[v6] == v4))
