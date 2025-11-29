# Time:  add:   O(n),
#        query: O(rlogn), r is the size of result
# Space: O(n)
import bisect
class TweetCounts2(object):

    def __init__(self):
        self.__records = collections.defaultdict(list)
        self.__lookup = {"minute":60, "hour":3600, "day":86400}

    def recordTweet(self, tweetName, time):
        """
        """
        bisect.insort(self.__records[tweetName], time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        """
        delta = self.__lookup[freq]
        i = startTime
        result = []
        while i <= endTime:
            j = min(i+delta, endTime+1)
            result.append(bisect.bisect_left(self.__records[tweetName], j) - \
                          bisect.bisect_left(self.__records[tweetName], i))
            i += delta
        return result

    
