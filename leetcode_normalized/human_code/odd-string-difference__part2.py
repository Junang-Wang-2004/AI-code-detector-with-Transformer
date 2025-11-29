import collections

class C1(object):

    def oddString(self, a1):
        """
        """
        v1 = collections.Counter((tuple((ord(w[i + 1]) - ord(w[i]) for v2 in range(len(w) - 1))) for v3 in a1))
        v4 = next((k for v5, v6 in v1.items() if v6 == 1))
        return next((v3 for v3 in a1 if tuple((ord(v3[v2 + 1]) - ord(v3[v2]) for v2 in range(len(v3) - 1))) == v4))
