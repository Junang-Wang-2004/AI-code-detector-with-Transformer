import heapq

class C1(object):

    def maximumProduct(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = a1
        heapq.heapify(v2)
        while a2:
            heapq.heappush(v2, heapq.heappop(v2) + 1)
            a2 -= 1
        return reduce(lambda x, y: x * y % v1, v2)
