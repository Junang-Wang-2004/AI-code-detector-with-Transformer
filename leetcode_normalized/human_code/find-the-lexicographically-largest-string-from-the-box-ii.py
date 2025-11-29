class C1(object):

    def answerString(self, a1, a2):
        """
        """
        if a2 == 1:
            return a1
        v1 = v2 = 0
        for v3 in range(1, len(a1)):
            if a1[v3] == a1[v1 + v2]:
                v2 += 1
            elif a1[v3] < a1[v1 + v2]:
                v2 = 0
            elif a1[v3] > a1[v1 + v2]:
                if a1[v3 - v2] >= a1[v3]:
                    v1 = v3 - v2
                else:
                    v1 = v3
                v2 = 0
        return a1[v1:len(a1) - max(a2 - 1 - v1, 0)]
