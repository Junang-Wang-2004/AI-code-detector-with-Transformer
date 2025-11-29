import collections

class C1(object):

    def twoOutOfThree(self, a1, a2, a3):
        """
        """
        v1 = 2
        v2 = collections.Counter()
        v3 = []
        for v4 in (a1, a2, a3):
            for v5 in set(v4):
                v2[v5] += 1
                if v2[v5] == v1:
                    v3.append(v5)
        return v3
