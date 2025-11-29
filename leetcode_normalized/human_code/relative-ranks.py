class C1(object):

    def findRelativeRanks(self, a1):
        """
        """
        v1 = sorted(a1)[::-1]
        v2 = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + list(map(str, list(range(4, len(a1) + 1))))
        return list(map(dict(list(zip(v1, v2))).get, a1))
