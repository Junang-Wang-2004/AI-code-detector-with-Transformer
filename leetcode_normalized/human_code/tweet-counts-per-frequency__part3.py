class C1(object):

    def __init__(self):
        self.__records = collections.defaultdict(list)
        self.__lookup = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, a1, a2):
        """
        """
        self.__records[a1].append(a2)

    def getTweetCountsPerFrequency(self, a1, a2, a3, a4):
        """
        """
        v1 = self.__lookup[a1]
        v2 = [0] * ((a4 - a3) // v1 + 1)
        for v3 in self.__records[a2]:
            if a3 <= v3 <= a4:
                v2[(v3 - a3) // v1] += 1
        return v2
