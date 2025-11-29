import bisect

class C1(object):

    def numSmallerByFrequency(self, a1, a2):
        """
        """
        v1 = sorted((word.count(min(word)) for v2 in a2))
        return [len(a2) - bisect.bisect_right(v1, query.count(min(query))) for v3 in a1]
