from random import randint, seed

class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a2
        self.nexts = [None] * a1
        self.prevs = [None] * a1

class C2(object):
    v1, v2 = (1, 2)
    v3 = 32

    def __init__(self, a1=[float('inf'), float('inf'), float('inf')], a2=True):
        seed(0)
        self.__head = C1()
        self.__len = 0
        self.__can_duplicated = a2
        self.add(a1)
        self.__end = self.find(a1)

    def begin(self):
        return self.__head.nexts[0]

    def end(self):
        return self.__end

    def lower_bound(self, a1, a2=lambda x, y: x < y):
        return self.__lower_bound(a1, self.__find_prev_nodes(a1, a2))

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

    def __find_prev_nodes(self, a1, a2=lambda x, y: x < y):
        v1 = [None] * len(self.__head.nexts)
        v2 = self.__head
        for v3 in reversed(range(len(self.__head.nexts))):
            while v2.nexts[v3] and a2(v2.nexts[v3].val, a1):
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

    def __init__(self):
        self.__skiplist = C2()

    def add(self, a1, a2):
        self.__skiplist.add([a1, a2, 0])
        v1 = self.__skiplist.find([a1, a2, 0])
        v2 = v3 = v1
        v1 = v1.nexts[0]
        while self.__intersect(v3, v1):
            v1 = self.__skiplist.remove(v1)
        if v2 != self.__skiplist.begin():
            v2 = v2.prevs[0]
            if self.__intersect(v2, v3):
                v3 = self.__skiplist.remove(v3)
                self.__intersect(v2, v3)
        v3 = v2
        while v3 != self.__skiplist.begin():
            v2 = v2.prevs[0]
            if v2.val[2] < v3.val[2]:
                break
            v3 = self.__skiplist.remove(v3)
            self.__intersect(v2, v3)
            v3 = v2

    def query(self, a1):
        v1 = self.__skiplist.lower_bound(a1, cmp=lambda x, y: a1[2] < y)
        return v1.val[0] * a1 + v1.val[1]

    def __intersect(self, a1, a2):
        if a2 == self.__skiplist.end():
            a1.val[2] = float('inf')
            return False
        if a1.val[0] == a2.val[0]:
            a1.val[2] = float('inf') if a1.val[1] > a2.val[1] else float('-inf')
        else:
            a1.val[2] = (a2.val[1] - a1.val[1]) // (a1.val[0] - a2.val[0])
        return a1.val[2] >= a2.val[2]

    def __iter__(self):
        return iter(self.__skiplist)

    def __len__(self):
        return len(self.__skiplist)

    def __str__(self):
        return str(self.__skiplist)

class C4(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = [0] * (len(a2) + 1)
        for v2 in range(len(a1)):
            v3[v2 + 1] = v3[v2] + a2[v2]
        v4 = 0
        v5 = C3()
        for v2 in reversed(range(len(a1))):
            v5.add(v1[v2 + 1], -(v4 + v1[v2 + 1] * v3[v2 + 1]))
            v4 = -v5.query(v3[v2]) + a3 * (v3[-1] - v3[v2])
        return v4
