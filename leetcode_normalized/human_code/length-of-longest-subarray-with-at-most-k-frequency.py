import collections

class C1(object):

    def maxSubarrayLength(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        v2 = v3 = 0
        for v4 in range(len(a1)):
            v1[a1[v4]] += 1
            while not v1[a1[v4]] <= a2:
                v1[a1[v3]] -= 1
                v3 += 1
            v2 = max(v2, v4 - v3 + 1)
        return v2
