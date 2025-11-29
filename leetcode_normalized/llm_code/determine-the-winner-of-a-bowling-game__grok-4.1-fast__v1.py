class C1(object):

    def isWinner(self, a1, a2):

        def get_score(a1):
            v1 = 0
            v2 = len(a1)
            for v3 in range(v2):
                v4 = 1
                if v3 > 0 and a1[v3 - 1] == 10:
                    v4 = 2
                if v3 > 1 and a1[v3 - 2] == 10:
                    v4 = 2
                v1 += a1[v3] * v4
            return v1
        v1 = get_score(a1)
        v2 = get_score(a2)
        if v1 > v2:
            return 1
        return 2 if v1 < v2 else 0
