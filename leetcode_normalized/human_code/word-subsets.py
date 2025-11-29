import collections

class C1(object):

    def wordSubsets(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        for v2 in a2:
            for v3, v4 in list(collections.Counter(v2).items()):
                v1[v3] = max(v1[v3], v4)
        v5 = []
        for v6 in a1:
            v1 = collections.Counter(v6)
            if all((v1[v3] >= v1[v3] for v3 in v1)):
                v5.append(v6)
        return v5
