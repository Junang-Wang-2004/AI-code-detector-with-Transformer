class C1(object):

    def topKFrequent(self, a1, a2):
        """
        """
        return [key for v1, v2 in collections.Counter(a1).most_common(a2)]
