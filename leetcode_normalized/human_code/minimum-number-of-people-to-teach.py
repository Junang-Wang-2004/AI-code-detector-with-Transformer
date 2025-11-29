import collections

class C1(object):

    def minimumTeachings(self, a1, a2, a3):
        """
        """
        v1 = list(map(set, a2))
        v2 = set((i - 1 for v3, v4 in a3 if not v1[v3 - 1] & v1[v4 - 1] for v5 in [v3, v4]))
        v6 = collections.Counter()
        for v5 in v2:
            v6 += collections.Counter(a2[v5])
        return len(v2) - max(list(v6.values()) + [0])
