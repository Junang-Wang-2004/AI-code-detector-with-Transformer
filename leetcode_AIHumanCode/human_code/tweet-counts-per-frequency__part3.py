# Time:  add:   O(1),
#        query: O(n)
# Space: O(n)
class TweetCounts3(object):

    def __init__(self):
        self.__records = collections.defaultdict(list)
        self.__lookup = {"minute":60, "hour":3600, "day":86400}

    def recordTweet(self, tweetName, time):
        """
        """
        self.__records[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        """
        delta = self.__lookup[freq]
        result = [0]*((endTime- startTime)//delta+1)
        for t in self.__records[tweetName]:
            if startTime <= t <= endTime:
                result[(t-startTime)//delta] += 1
        return result
