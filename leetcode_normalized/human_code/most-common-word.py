import collections

class C1(object):

    def mostCommonWord(self, a1, a2):
        """
        """
        v1 = set(a2)
        v2 = collections.Counter((word.strip("!?',.") for v3 in a1.lower().split()))
        v4 = ''
        for v3 in v2:
            if (not v4 or v2[v3] > v2[v4]) and v3 not in v1:
                v4 = v3
        return v4
