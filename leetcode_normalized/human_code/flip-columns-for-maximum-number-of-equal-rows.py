import collections

class C1(object):

    def maxEqualRowsAfterFlips(self, a1):
        """
        """
        v1 = collections.Counter((tuple((x ^ row[0] for v2 in row)) for v3 in a1))
        return max(v1.values())
