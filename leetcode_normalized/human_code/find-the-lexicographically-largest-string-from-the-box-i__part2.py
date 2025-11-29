class C1(object):

    def answerString(self, a1, a2):
        """
        """
        if a2 == 1:
            return a1
        v1 = len(a1) - (a2 - 1)
        v2 = max(a1)
        return max((a1[i:i + v1] for v3 in range(len(a1)) if a1[v3] == v2))
