import collections

class C1(object):

    def frequencySort(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        return sorted(a1, key=lambda x: (v1[x], -x))
