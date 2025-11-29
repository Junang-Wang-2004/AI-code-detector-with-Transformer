class C1(object):

    def pathExistenceQueries(self, a1, a2, a3, a4):
        """
        """
        v1 = [0] * a1
        for v2 in range(a1 - 1):
            v1[v2 + 1] = v1[v2] + int(a2[v2 + 1] - a2[v2] > a3)
        return [v1[v2] == v1[j] for v2, v3 in a4]
