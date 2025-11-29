from sortedcontainers import SortedList
import collections

class StatisticsTracker(object):

    def __init__(self):
        self._total = 0
        self._queue = collections.deque()
        self._small = SortedList()
        self._large = SortedList()
        self._occurrences = collections.Counter()
        self._numbers_per_occur = {}
        self._ordered_occur = SortedList()

    def _modify_frequency(self, value, increment):
        old_frequency = self._occurrences[value]
        if old_frequency > 0:
            self._numbers_per_occur[old_frequency].remove(value)
            if len(self._numbers_per_occur[old_frequency]) == 0:
                del self._numbers_per_occur[old_frequency]
                self._ordered_occur.remove(old_frequency)
        self._occurrences[value] += increment
        new_frequency = self._occurrences[value]
        if new_frequency > 0:
            if new_frequency not in self._numbers_per_occur:
                self._numbers_per_occur[new_frequency] = SortedList()
                self._ordered_occur.add(new_frequency)
            self._numbers_per_occur[new_frequency].add(value)
        else:
            del self._occurrences[value]

    def _equalize_halves(self):
        if len(self._large) == len(self._small) + 2:
            self._small.add(self._large.pop(0))
        elif len(self._small) == len(self._large) + 1:
            self._large.add(self._small.pop())

    def addNumber(self, value):
        self._total += value
        self._queue.append(value)
        self._modify_frequency(value, 1)
        if not self._large or value >= self._large[0]:
            self._large.add(value)
        else:
            self._small.add(value)
        self._equalize_halves()

    def removeFirstAddedNumber(self):
        value = self._queue.popleft()
        self._total -= value
        self._modify_frequency(value, -1)
        if value in self._large:
            self._large.remove(value)
        else:
            self._small.remove(value)
        self._equalize_halves()

    def getMean(self):
        return self._total // len(self._queue)

    def getMedian(self):
        return self._large[0]

    def getMode(self):
        return self._numbers_per_occur[self._ordered_occur[-1]][0]
