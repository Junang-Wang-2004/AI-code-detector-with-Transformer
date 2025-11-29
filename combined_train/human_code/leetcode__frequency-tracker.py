class C1(object):

    def __init__(self):
        self.__cnt = collections.Counter()
        self.__freq = collections.Counter()

    def add(self, a1):
        """
        """
        self.__freq[self.__cnt[a1]] -= 1
        if self.__freq[self.__cnt[a1]] == 0:
            del self.__freq[self.__cnt[a1]]
        self.__cnt[a1] += 1
        self.__freq[self.__cnt[a1]] += 1

    def deleteOne(self, a1):
        """
        """
        if self.__cnt[a1] == 0:
            return
        self.__freq[self.__cnt[a1]] -= 1
        if self.__freq[self.__cnt[a1]] == 0:
            del self.__freq[self.__cnt[a1]]
        self.__cnt[a1] -= 1
        self.__freq[self.__cnt[a1]] += 1
        if self.__cnt[a1] == 0:
            del self.__cnt[a1]

    def hasFrequency(self, a1):
        """
        """
        return a1 in self.__freq
