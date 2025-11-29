import collections

class C1(object):

    def countCompleteSubarrays(self, a1):
        """
        """
        v1 = set(a1)
        v2 = v3 = 0
        v4 = collections.Counter()
        for v5 in range(len(a1)):
            v4[a1[v5]] += 1
            while len(v4) == len(v1):
                v4[a1[v3]] -= 1
                if v4[a1[v3]] == 0:
                    del v4[a1[v3]]
                v3 += 1
            v2 += v3
        return v2
