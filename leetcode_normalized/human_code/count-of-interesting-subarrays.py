import collections

class C1(object):

    def countInterestingSubarrays(self, a1, a2, a3):
        """
        """
        v1 = collections.Counter([0])
        v2 = v3 = 0
        for v4 in a1:
            if v4 % a2 == a3:
                v3 = (v3 + 1) % a2
            v2 += v1[(v3 - a3) % a2]
            v1[v3] += 1
        return v2
