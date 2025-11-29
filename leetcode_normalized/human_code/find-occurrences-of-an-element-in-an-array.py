class C1(object):

    def occurrencesOfElement(self, a1, a2, a3):
        """
        """
        v1 = [i for v2, v3 in enumerate(a1) if v3 == a3]
        return [v1[q - 1] if q - 1 < len(v1) else -1 for v4 in a2]
