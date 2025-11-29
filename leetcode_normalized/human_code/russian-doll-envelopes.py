class C1(object):

    def maxEnvelopes(self, a1):
        """
        """

        def insert(a1):
            v1, v2 = (0, len(result) - 1)
            while v1 <= v2:
                v3 = v1 + (v2 - v1) / 2
                if result[v3] >= a1:
                    v2 = v3 - 1
                else:
                    v1 = v3 + 1
            if v1 == len(result):
                result.append(a1)
            else:
                result[v1] = a1
        v1 = []
        a1.sort(lambda x, y: y[1] - x[1] if x[0] == y[0] else x[0] - y[0])
        for v2 in a1:
            insert(v2[1])
        return len(v1)
