import collections

class C1(object):

    def divisibleTripletCount(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3 = collections.Counter()
            for v4 in range(v2 + 1, len(a1)):
                v1 += v3[a1[v4] % a2]
                v3[-(a1[v2] + a1[v4]) % a2] += 1
        return v1
