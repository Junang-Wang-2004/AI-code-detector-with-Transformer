import collections

class C1(object):

    def sumPrefixScores(self, a1):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a1:
            v4 = v2
            for v5 in v3:
                v4 = v4[v5]
                v4['_cnt'] = v4['_cnt'] + 1 if '_cnt' in v4 else 1
        v6 = []
        for v3 in a1:
            v7 = 0
            v4 = v2
            for v5 in v3:
                v4 = v4[v5]
                v7 += v4['_cnt']
            v6.append(v7)
        return v6
