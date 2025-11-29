import collections

class C1(object):

    def countSubarrays(self, a1, a2):
        """
        """
        v1 = 0
        v2 = collections.defaultdict(int)
        for v3 in a1:
            v4 = collections.defaultdict(int)
            if v3 & a2 == a2:
                v4[v3] += 1
                for v5, v6 in v2.items():
                    v4[v5 & v3] += v6
                if a2 in v4:
                    v1 += v4[a2]
            v2 = v4
        return v1
