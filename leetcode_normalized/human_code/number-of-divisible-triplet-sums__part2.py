import collections

class C1(object):

    def divisibleTripletCount(self, a1, a2):
        """
        """
        v1 = 0
        v2 = collections.Counter()
        for v3 in range(len(a1)):
            if a1[v3] % a2 in v2:
                v1 += v2[a1[v3] % a2]
            for v4 in range(v3):
                v2[-(a1[v3] + a1[v4]) % a2] += 1
        return v1
