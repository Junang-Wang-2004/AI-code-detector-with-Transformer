import collections
from random import randint, seed

class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a2
        self.nexts = [None] * a1
        self.prevs = [None] * a1

class C2(object):
    v1, v2 = (1, 2)
    v3 = 32

    def __init__(self, a1=float('inf'), a2=False, a3=lambda x, y: x < y):
        seed(0)
        self.__head = C1()
        self.__len = 0
        self.__can_duplicated = a2
        self.__cmp = a3
        self.add(a1)
        self.__end = self.find(a1)

    def begin(self):
        return self.__head.nexts[0]

    def end(self):
        return self.__end

    def lower_bound(self, a1):
        return self.__lower_bound(a1, self.__find_prev_nodes(a1))

    def find(self, a1):
        return self.__find(a1, self.__find_prev_nodes(a1))

    def add(self, a1):
        if not self.__can_duplicated and self.find(a1):
            return (self.find(a1), False)
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
        return v1 if self.__can_duplicated else (v1, True)

    def remove(self, a1):
        v1 = a1.prevs
        v2 = self.__find(a1.val, v1)
        if not v2:
            return self.__end
        self.__len -= 1
        for v3 in reversed(range(len(v2.nexts))):
            v1[v3].nexts[v3] = v2.nexts[v3]
            if v2.nexts[v3]:
                v2.nexts[v3].prevs[v3] = v1[v3]
            if not self.__head.nexts[v3]:
                self.__head.nexts.pop()
        return v2.nexts[0]

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
            while v2.nexts[v3] and self.__cmp(v2.nexts[v3].val, a1):
                v2 = v2.nexts[v3]
            v1[v3] = v2
        return v1

    def __random_level(self):
        v1 = 1
        while randint(1, C2.P_DENOMINATOR) <= C2.P_NUMERATOR and v1 < C2.MAX_LEVEL:
            v1 += 1
        return v1

    def __iter__(self):
        v1 = self.begin()
        while v1 != self.end():
            yield v1.val
            v1 = v1.nexts[0]

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

    def minimumIncompatibility(self, a1, a2):
        """
        """

        def greedy(a1, a2, a3):
            v1 = collections.Counter(a1)
            if max(v1.values()) > a2:
                return -1
            v2 = C2() if not a3 else C2(end=float('-inf'), cmp=lambda x, y: x > y)
            v3 = collections.defaultdict(collections.OrderedDict)
            for v4 in sorted(list(v1.keys()), reverse=a3):
                v2.add(v4)
                v3[v1[v4]][v4] = v1[v4]
            v5 = [[] for v6 in range(a2)]
            v7 = 0
            while v2:
                if len(v5) - v7 in v3:
                    for v4 in v3[len(v5) - v7].keys():
                        for v8 in range(v7, len(v5)):
                            v5[v8].append(v4)
                        v1.pop(v4)
                        v2.remove(v2.find(v4))
                    v3.pop(len(v5) - v7)
                v9 = v2.begin()
                while v9 != v2.end():
                    v4 = v9.val
                    v5[v7].append(v4)
                    v3[v1[v4]].pop(v4)
                    if not v3[v1[v4]]:
                        v3.pop(v1[v4])
                    v1[v4] -= 1
                    if not v1[v4]:
                        v1.pop(v4)
                        v9 = v2.remove(v9)
                    else:
                        v3[v1[v4]][v4] = v1[v4]
                        v9 = v9.nexts[0]
                    if len(v5[v7]) == len(a1) // a2:
                        v7 += 1
                        break
            return sum([max(stk) - min(stk) for v10 in v5])
        return min(greedy(a1, a2, False), greedy(a1, a2, True))
