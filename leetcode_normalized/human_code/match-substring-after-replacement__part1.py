import collections

class C1(object):

    def matchReplacement(self, a1, a2, a3):
        """
        """

        def transform(a1):
            return ord(a1) - ord('0') if a1.isdigit() else ord(a1) - ord('a') + 10 if a1.islower() else ord(a1) - ord('A') + 36

        def check(a1):
            return all((a2[j] == a1[a1 + j] or lookup[a2[j]][a1[a1 + j]] for v1 in range(len(a2))))
        v1 = [[0] * 62 for v2 in range(62)]
        for v3, v4 in a3:
            v1[transform(v3)][transform(v4)] = 1
        a1 = list(map(transform, a1))
        a2 = list(map(transform, a2))
        return any((check(i) for v7 in range(len(a1) - len(a2) + 1)))
