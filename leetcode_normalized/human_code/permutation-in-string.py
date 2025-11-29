import collections

class C1(object):

    def checkInclusion(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = len(a1)
        for v3 in range(len(a2)):
            if v1[a2[v3]] > 0:
                v2 -= 1
            v1[a2[v3]] -= 1
            if v2 == 0:
                return True
            v4 = v3 + 1 - len(a1)
            if v4 >= 0:
                v1[a2[v4]] += 1
                if v1[a2[v4]] > 0:
                    v2 += 1
        return False
