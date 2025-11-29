import collections

class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * a1

    def add(self, a1, a2):
        while a1 < len(self.__bit):
            self.__bit[a1] += a2
            a1 += a1 & -a1

    def sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.__bit[a1]
            a1 -= a1 & -a1
        return v1

class C2(object):

    def minInteger(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(list)
        v2 = C1(len(a1) + 1)
        for v3 in reversed(range(len(a1))):
            v2.add(v3 + 1, 1)
            v1[int(a1[v3])].append(v3 + 1)
        v4 = []
        for v5 in range(len(a1)):
            for v6 in range(10):
                if v1[v6] and v2.sum(v1[v6][-1] - 1) <= a2:
                    a2 -= v2.sum(v1[v6][-1] - 1)
                    v2.add(v1[v6].pop(), -1)
                    v4.append(v6)
                    break
        return ''.join(map(str, v4))
