import collections

class C1(object):

    def bestTeamScore(self, a1, a2):
        """
        """
        v1 = sorted(zip(a1, a2))
        v2 = sorted(set(a2))
        v3 = collections.defaultdict(int)
        v4 = 0
        for v5, v6 in v1:
            v3[v6] = max((v3[a] for v7 in v2 if v7 <= v6)) + v5
        return max(v3.values())
