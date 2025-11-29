import collections
import random

class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a2
        self.nexts = [None] * a1
        self.prevs = [None] * a1

class C2(object):
    v1, v2 = (1, 2)
    v3 = 32

    def __init__(self, a1=float('inf'), a2=False):
        random.seed(0)
        self.__head = C1()
        self.__len = 0
        self.__can_duplicated = a2
        self.add(a1)

    def lower_bound(self, a1):
        return self.__lower_bound(a1, self.__find_prev_nodes(a1))

    def find(self, a1):
        return self.__find(a1, self.__find_prev_nodes(a1))

    def add(self, a1):
        if not self.__can_duplicated and self.find(a1):
            return False
        v1 = C1(self.__random_level(), a1)
        if len(self.__head.nexts) < len(v1.nexts):
            self.__head.nexts.extend([None] * (len(v1.nexts) - len(self.__head.nexts)))
        v2 = self.__find_prev_nodes(a1)
        for v3 in range(len(v1.nexts)):
            v1.nexts[v3] = v2[v3].nexts[v3]
            if v2[v3].nexts[v3]:
                v2[v3].nexts[v3].prevs[v3] = v1
            v2[v3].nexts[v3] = v1
            v1.prevs[v3] = v2[v3]
        self.__len += 1
        return True

    def remove(self, a1):
        v1 = self.__find_prev_nodes(a1)
        v2 = self.__find(a1, v1)
        if not v2:
            return False
        self.__len -= 1
        for v3 in reversed(range(len(v2.nexts))):
            v1[v3].nexts[v3] = v2.nexts[v3]
            if v2.nexts[v3]:
                v2.nexts[v3].prevs[v3] = v1[v3]
            if not self.__head.nexts[v3]:
                self.__head.nexts.pop()
        return True

    def __lower_bound(self, a1, a2):
        if a2:
            v1 = a2[0].nexts[0]
            if v1:
                return v1
        return None

    def __find(self, a1, a2):
        v1 = self.__lower_bound(a1, a2)
        if v1 and v1.val == a1:
            return v1
        return None

    def __find_prev_nodes(self, a1):
        v1 = [None] * len(self.__head.nexts)
        v2 = self.__head
        for v3 in reversed(range(len(self.__head.nexts))):
            while v2.nexts[v3] and v2.nexts[v3].val < a1:
                v2 = v2.nexts[v3]
            v1[v3] = v2
        return v1

    def __random_level(self):
        v1 = 1
        while random.randint(1, C2.P_DENOMINATOR) <= C2.P_NUMERATOR and v1 < C2.MAX_LEVEL:
            v1 += 1
        return v1

    def __len__(self):
        return self.__len - 1

    def __str__(self):
        v1 = []
        for v2 in reversed(range(len(self.__head.nexts))):
            v1.append([])
            v3 = self.__head.nexts[v2]
            while v3:
                v1[-1].append(str(v3.val))
                v3 = v3.nexts[v2]
        return '\n'.join(['->'.join(x) for v4 in v1])

class C3(object):

    def __init__(self):
        self.__records = collections.defaultdict(lambda: C2(can_duplicated=True))
        self.__lookup = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, a1, a2):
        """
        """
        self.__records[a1].add(a2)

    def getTweetCountsPerFrequency(self, a1, a2, a3, a4):
        """
        """
        v1 = self.__lookup[a1]
        v2 = [0] * ((a4 - a3) // v1 + 1)
        v3 = self.__records[a2].lower_bound(a3)
        while v3 is not None and v3.val <= a4:
            v2[(v3.val - a3) // v1] += 1
            v3 = v3.nexts[0]
        return v2
