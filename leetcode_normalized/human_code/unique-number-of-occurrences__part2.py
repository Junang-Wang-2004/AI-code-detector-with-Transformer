class C1(object):

    def uniqueOccurrences(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        return len(v1) == len(set(v1.values()))
