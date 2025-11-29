import heapq

class C1(object):
    v1 = sorted((2 ** a * 3 ** b * 5 ** c for v2 in range(32) for v3 in range(20) for v4 in range(14)))

    def nthUglyNumber(self, a1):
        return self.ugly[a1 - 1]
