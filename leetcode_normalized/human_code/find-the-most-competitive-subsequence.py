class C1(object):

    def mostCompetitive(self, a1, a2):
        """
        """
        v1 = []
        for v2, v3 in enumerate(a1):
            while v1 and v1[-1] > v3 and (len(v1) + (len(a1) - v2) > a2):
                v1.pop()
            if len(v1) < a2:
                v1.append(v3)
        return v1
