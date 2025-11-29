import itertools

class C1(object):

    def numOfSubarrays(self, a1, a2, a3):
        """
        """
        v1, v2 = (0, sum(itertools.islice(a1, 0, a2 - 1)))
        for v3 in range(a2 - 1, len(a1)):
            v2 += a1[v3] - (a1[v3 - a2] if v3 - a2 >= 0 else 0)
            v1 += int(v2 >= a3 * a2)
        return v1
