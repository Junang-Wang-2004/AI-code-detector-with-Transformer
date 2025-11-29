class C1(object):

    def maxValue(self, a1, a2):
        """
        """
        v1 = (lambda i: str(a2) > a1[i]) if a1[0] != '-' else lambda i: str(a2) < a1[i]
        for v2 in range(len(a1)):
            if v1(v2):
                break
        else:
            v2 = len(a1)
        return a1[:v2] + str(a2) + a1[v2:]
