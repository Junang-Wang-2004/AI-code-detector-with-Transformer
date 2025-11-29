from sortedcontainers import SortedList
import collections

class C1(object):

    def __init__(self):
        self._total = 0
        self._queue = collections.deque()
        self._small = SortedList()
        self._large = SortedList()
        self._occurrences = collections.Counter()
        self._numbers_per_occur = {}
        self._ordered_occur = SortedList()

    def _modify_frequency(self, a1, a2):
        v1 = self._occurrences[a1]
        if v1 > 0:
            self._numbers_per_occur[v1].remove(a1)
            if len(self._numbers_per_occur[v1]) == 0:
                del self._numbers_per_occur[v1]
                self._ordered_occur.remove(v1)
        self._occurrences[a1] += a2
        v2 = self._occurrences[a1]
        if v2 > 0:
            if v2 not in self._numbers_per_occur:
                self._numbers_per_occur[v2] = SortedList()
                self._ordered_occur.add(v2)
            self._numbers_per_occur[v2].add(a1)
        else:
            del self._occurrences[a1]

    def _equalize_halves(self):
        if len(self._large) == len(self._small) + 2:
            self._small.add(self._large.pop(0))
        elif len(self._small) == len(self._large) + 1:
            self._large.add(self._small.pop())

    def addNumber(self, a1):
        self._total += a1
        self._queue.append(a1)
        self._modify_frequency(a1, 1)
        if not self._large or a1 >= self._large[0]:
            self._large.add(a1)
        else:
            self._small.add(a1)
        self._equalize_halves()

    def removeFirstAddedNumber(self):
        v1 = self._queue.popleft()
        self._total -= v1
        self._modify_frequency(v1, -1)
        if v1 in self._large:
            self._large.remove(v1)
        else:
            self._small.remove(v1)
        self._equalize_halves()

    def getMean(self):
        return self._total // len(self._queue)

    def getMedian(self):
        return self._large[0]

    def getMode(self):
        return self._numbers_per_occur[self._ordered_occur[-1]][0]
