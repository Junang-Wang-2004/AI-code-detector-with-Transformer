class C1(object):

    def removeDigit(self, a1, a2):
        """
        """
        v1 = next((v1 for v1 in range(len(a1) - 1) if a2 == a1[v1] < a1[v1 + 1]), len(a1) - 1)
        if v1 + 1 == len(a1):
            v1 = next((v1 for v1 in reversed(range(len(a1))) if a2 == a1[v1]))
        return a1[:v1] + a1[v1 + 1:]
