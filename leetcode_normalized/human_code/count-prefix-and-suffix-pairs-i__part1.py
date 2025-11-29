import collections

class C1(object):

    def countPrefixSuffixPairs(self, a1):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        v3 = 0
        for v4 in a1:
            v5 = v2
            for v6 in range(len(v4)):
                v5 = v5[v4[v6], v4[~v6]]
                v3 += v5['_cnt'] if '_cnt' in v5 else 0
            v5['_cnt'] = v5['_cnt'] + 1 if '_cnt' in v5 else 1
        return v3
