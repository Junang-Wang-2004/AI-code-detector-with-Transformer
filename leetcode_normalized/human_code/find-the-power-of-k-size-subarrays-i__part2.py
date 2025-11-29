class C1(object):

    def resultsArray(self, a1, a2):
        """
        """
        return [a1[i + a2 - 1] if all((a1[j] + 1 == a1[j + 1] for v1 in range(i, i + a2 - 1))) else -1 for v2 in range(len(a1) - a2 + 1)]
