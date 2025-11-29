import heapq

class C1(object):

    def nthUglyNumber(self, a1):
        v1 = 0
        v2 = []
        heapq.heappush(v2, 1)
        for v3 in range(a1):
            v1 = heapq.heappop(v2)
            if v1 % 2 == 0:
                heapq.heappush(v2, v1 * 2)
            elif v1 % 3 == 0:
                heapq.heappush(v2, v1 * 2)
                heapq.heappush(v2, v1 * 3)
            else:
                heapq.heappush(v2, v1 * 2)
                heapq.heappush(v2, v1 * 3)
                heapq.heappush(v2, v1 * 5)
        return v1

    def nthUglyNumber2(self, a1):
        v1 = [1]
        v2 = v3 = v4 = 0
        while len(v1) < a1:
            while v1[v2] * 2 <= v1[-1]:
                v2 += 1
            while v1[v3] * 3 <= v1[-1]:
                v3 += 1
            while v1[v4] * 5 <= v1[-1]:
                v4 += 1
            v1.append(min(v1[v2] * 2, v1[v3] * 3, v1[v4] * 5))
        return v1[-1]

    def nthUglyNumber3(self, a1):
        v1, v2, v3 = ([2], [3], [5])
        v4 = 1
        for v5 in heapq.merge(v1, v2, v3):
            if a1 == 1:
                return v4
            if v5 > v4:
                v4 = v5
                a1 -= 1
                v1 += (2 * v5,)
                v2 += (3 * v5,)
                v3 += (5 * v5,)
