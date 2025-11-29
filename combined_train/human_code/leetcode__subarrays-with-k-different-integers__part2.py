class C1(object):

    def __init__(self):
        self.__count = collections.defaultdict(int)

    def add(self, a1):
        self.__count[a1] += 1

    def remove(self, a1):
        self.__count[a1] -= 1
        if self.__count[a1] == 0:
            self.__count.pop(a1)

    def size(self):
        return len(self.__count)

class C2(object):

    def subarraysWithKDistinct(self, a1, a2):
        """
        """
        v1, v2 = (C1(), C1())
        v3, v4, v5 = (0, 0, 0)
        for v6 in a1:
            v1.add(v6)
            while v1.size() > a2:
                v1.remove(a1[v4])
                v4 += 1
            v2.add(v6)
            while v2.size() >= a2:
                v2.remove(a1[v5])
                v5 += 1
            v3 += v5 - v4
        return v3
