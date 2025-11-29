import collections
import itertools

class C1(object):

    def findSecretWord(self, a1, a2):
        """
        """
        v1 = list(range(len(a1)))
        v2 = 0
        while v2 < 6:
            v3 = [collections.Counter((w[i] for v4 in a1)) for v5 in range(6)]
            v6 = max(v1, key=lambda x: sum((v3[v5][c] for v5, v7 in enumerate(a1[x]))))
            v2 = a2.guess(a1[v6])
            v1 = [j for v8 in v1 if sum((a == b for v9, v10 in zip(a1[v6], a1[v8]))) == v2]
