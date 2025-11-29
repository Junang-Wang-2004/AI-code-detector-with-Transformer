class C1(object):

    def findJudge(self, a1, a2):
        """
        """
        v1 = [0] * a1
        for v2, v3 in a2:
            v1[v2 - 1] -= 1
            v1[v3 - 1] += 1
        for v2 in range(len(v1)):
            if v1[v2] == a1 - 1:
                return v2 + 1
        return -1
