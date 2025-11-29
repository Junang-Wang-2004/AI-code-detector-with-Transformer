class C1(object):

    def goodDaysToRobBank(self, a1, a2):
        """
        """
        v1 = [0]
        for v2 in reversed(range(1, len(a1))):
            v1.append(v1[-1] + 1 if a1[v2] >= a1[v2 - 1] else 0)
        v1.reverse()
        v3 = []
        v4 = 0
        for v2 in range(len(a1)):
            if v4 >= a2 and v1[v2] >= a2:
                v3.append(v2)
            if v2 + 1 < len(a1):
                v4 = v4 + 1 if a1[v2] >= a1[v2 + 1] else 0
        return v3
