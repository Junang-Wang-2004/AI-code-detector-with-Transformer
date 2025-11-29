import collections

class C1(object):

    def __init__(self):
        self.__freq = collections.Counter()
        self.__group = collections.defaultdict(list)
        self.__maxfreq = 0

    def push(self, a1):
        """
        """
        self.__freq[a1] += 1
        if self.__freq[a1] > self.__maxfreq:
            self.__maxfreq = self.__freq[a1]
        self.__group[self.__freq[a1]].append(a1)

    def pop(self):
        """
        """
        v1 = self.__group[self.__maxfreq].pop()
        if not self.__group[self.__maxfreq]:
            self.__group.pop(self.__maxfreq)
            self.__maxfreq -= 1
        self.__freq[v1] -= 1
        if not self.__freq[v1]:
            self.__freq.pop(v1)
        return v1
