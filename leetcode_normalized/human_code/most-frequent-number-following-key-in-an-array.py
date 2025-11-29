import collections

class C1(object):

    def mostFrequent(self, a1, a2):
        """
        """
        return collections.Counter((a1[i + 1] for v1 in range(len(a1) - 1) if a1[v1] == a2)).most_common(1)[0][0]
