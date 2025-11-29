import collections

class C1(object):

    def frequencySort(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        v3 = [''] * (len(a1) + 1)
        for v2 in v1:
            v3[v1[v2]] += v2
        v4 = ''
        for v5 in reversed(range(len(v3) - 1)):
            for v2 in v3[v5]:
                v4 += v2 * v5
        return v4
