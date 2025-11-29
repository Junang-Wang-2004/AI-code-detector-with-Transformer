import collections
import sortedcontainers
import bisect

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__snaps = collections.defaultdict(lambda: sortedcontainers.SortedList([(0, 0)]))

    def set(self, a1, a2, a3):
        """
        """
        v1 = self.__snaps[a1].bisect_left((a3, float('-inf')))
        if v1 != len(self.__snaps[a1]) and self.__snaps[a1][v1][0] == a3:
            self.__snaps[a1].remove(self.__snaps[a1][v1])
        self.__snaps[a1].add((a3, a2))

    def get(self, a1, a2):
        """
        """
        v1 = self.__snaps[a1].bisect_left((a2 + 1, float('-inf'))) - 1
        return self.__snaps[a1][v1][1]

class C2(object):

    def __init__(self, a1):
        self.snap_id = 0
        self.set = C1(a1)
        for v1 in range(a1):
            self.set.set(v1, v1, self.snap_id)
        self.rank = C1(a1)

    def find_set(self, a1, a2):
        v1 = []
        while self.set.get(a1, a2) != a1:
            v1.append(a1)
            a1 = self.set.get(a1, a2)
        while v1:
            self.set.set(v1.pop(), a1, a2)
        return a1

    def union_set(self, a1, a2):
        v1 = self.find_set(a1, self.snap_id)
        v2 = self.find_set(a2, self.snap_id)
        if v1 == v2:
            return False
        if self.rank.get(v1, self.snap_id) < self.rank.get(v2, self.snap_id):
            self.set.set(v1, v2, self.snap_id)
        elif self.rank.get(v1, self.snap_id) > self.rank.get(v2, self.snap_id):
            self.set.set(v2, v1, self.snap_id)
        else:
            self.set.set(v2, v1, self.snap_id)
            self.rank.set(v1, self.rank.get(v1, self.snap_id) + 1, self.snap_id)
        return True

    def snap(self):
        self.snap_id += 1

class C3(object):

    def __init__(self, a1, a2):
        """
        """
        a2.sort(key=lambda x: x[2])
        self.__uf = C2(a1)
        self.__weights = []
        for v1, (v2, v3, v4) in enumerate(a2):
            if not self.__uf.union_set(v2, v3):
                continue
            self.__uf.snap()
            self.__weights.append(v4)

    def query(self, a1, a2, a3):
        """
        """
        v1 = bisect.bisect_left(self.__weights, a3) - 1
        if v1 == -1:
            return False
        return self.__uf.find_set(a1, v1) == self.__uf.find_set(a2, v1)
