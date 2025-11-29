import collections

class C1(object):

    def numGoodSubarrays(self, a1, a2):
        """
        """
        v1 = v2 = 0
        v3 = collections.defaultdict(int)
        v3[0] = 1
        v4 = 0
        while v4 < len(a1):
            v5, v6 = (v4, v2)
            while v5 < len(a1) and a1[v5] == a1[v4]:
                v6 = (v6 + a1[v5]) % a2
                v1 += v3[v6]
                v5 += 1
            while v4 < v5:
                v2 = (v2 + a1[v4]) % a2
                v3[v2] += 1
                v4 += 1
        return v1
