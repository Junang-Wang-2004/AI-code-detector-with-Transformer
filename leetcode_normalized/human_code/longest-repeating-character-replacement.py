import collections

class C1(object):

    def characterReplacement(self, a1, a2):
        """
        """
        v1, v2 = (0, 0)
        v3 = collections.Counter()
        for v4 in range(len(a1)):
            v3[a1[v4]] += 1
            v2 = max(v2, v3[a1[v4]])
            if v1 - v2 >= a2:
                v3[a1[v4 - v1]] -= 1
            else:
                v1 += 1
        return v1
