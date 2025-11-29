from sortedcontainers import SortedList
import collections

class C1(object):

    def __init__(self):
        self.__total = 0
        self.__dq = collections.deque()
        self.__sl1 = SortedList()
        self.__sl2 = SortedList()
        self.__num_to_freq = collections.defaultdict(int)
        self.__sorted_freqs = SortedList()
        self.__freq_to_nums = collections.defaultdict(SortedList)

    def __update(self, a1, a2):
        if a1 in self.__num_to_freq:
            self.__freq_to_nums[self.__num_to_freq[a1]].remove(a1)
            if not self.__freq_to_nums[self.__num_to_freq[a1]]:
                del self.__freq_to_nums[self.__num_to_freq[a1]]
                self.__sorted_freqs.remove(self.__num_to_freq[a1])
        self.__num_to_freq[a1] += a2
        if not self.__num_to_freq[a1]:
            del self.__num_to_freq[a1]
        else:
            if not self.__freq_to_nums[self.__num_to_freq[a1]]:
                self.__sorted_freqs.add(self.__num_to_freq[a1])
            self.__freq_to_nums[self.__num_to_freq[a1]].add(a1)

    def __rebalance(self):
        if len(self.__sl2) == len(self.__sl1) + 2:
            self.__sl1.add(self.__sl2.pop(0))
        elif len(self.__sl2) + 1 == len(self.__sl1):
            self.__sl2.add(self.__sl1.pop(-1))

    def addNumber(self, a1):
        """
        """
        self.__total += a1
        self.__dq.append(a1)
        self.__update(a1, +1)
        (self.__sl2 if not self.__sl2 or self.__sl2[0] <= a1 else self.__sl1).add(a1)
        self.__rebalance()

    def removeFirstAddedNumber(self):
        """
        """
        v1 = self.__dq.popleft()
        self.__total -= v1
        self.__update(v1, -1)
        (self.__sl2 if v1 in self.__sl2 else self.__sl1).remove(v1)
        self.__rebalance()

    def getMean(self):
        """
        """
        return self.__total // len(self.__dq)

    def getMedian(self):
        """
        """
        return self.__sl2[0]

    def getMode(self):
        """
        """
        return self.__freq_to_nums[self.__sorted_freqs[-1]][0]
