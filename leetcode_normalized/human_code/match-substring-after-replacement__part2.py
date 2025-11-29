import collections

class C1(object):

    def matchReplacement(self, a1, a2, a3):
        """
        """

        def check(a1):
            return all((a2[j] == a1[a1 + j] or (a2[j], a1[a1 + j]) in lookup for v1 in range(len(a2))))
        v1 = set()
        for v2, v3 in a3:
            v1.add((v2, v3))
        return any((check(i) for v4 in range(len(a1) - len(a2) + 1)))
