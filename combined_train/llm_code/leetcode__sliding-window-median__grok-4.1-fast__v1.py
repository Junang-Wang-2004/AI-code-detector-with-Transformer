import collections
import heapq

class C1:

    def medianSlidingWindow(self, a1, a2):
        v1 = []
        v2 = []
        v3 = collections.defaultdict(int)

        def purge(a1, a2):
            while a1 and a2 * a1[0] in v3:
                v1 = a2 * a1[0]
                v3[v1] -= 1
                if v3[v1] == 0:
                    del v3[v1]
                heapq.heappop(a1)

        def restore():
            v1 = []
            for v2 in v1:
                v3 = -v2
                if v3 not in v3 or v3[v3] == 0:
                    v1.append(v3)
                else:
                    v3[v3] -= 1
                    if v3[v3] == 0:
                        del v3[v3]
            for v3 in v2:
                if v3 not in v3 or v3[v3] == 0:
                    v1.append(v3)
                else:
                    v3[v3] -= 1
                    if v3[v3] == 0:
                        del v3[v3]
            v1.clear()
            v2.clear()
            v1.sort()
            v4 = (a2 + 1) // 2
            for v5 in range(v4):
                heapq.heappush(v1, -v1[v5])
            for v5 in range(v4, a2):
                heapq.heappush(v2, v1[v5])
        v4 = []
        for v5 in a1[:a2]:
            if len(v1) == 0 or v5 <= -v1[0]:
                heapq.heappush(v1, -v5)
            else:
                heapq.heappush(v2, v5)
            if len(v1) > len(v2) + 1:
                heapq.heappush(v2, -heapq.heappop(v1))
            if len(v2) > len(v1):
                heapq.heappush(v1, -heapq.heappop(v2))
        purge(v1, -1)
        purge(v2, 1)
        v6 = float(-v1[0]) if a2 % 2 else (-v1[0] + v2[0]) / 2
        v4.append(v6)
        for v7 in range(a2, len(a1)):
            v3[a1[v7 - a2]] += 1
            v5 = a1[v7]
            purge(v1, -1)
            purge(v2, 1)
            if len(v1) == 0 or v5 <= -v1[0]:
                heapq.heappush(v1, -v5)
            else:
                heapq.heappush(v2, v5)
            if len(v1) > len(v2) + 1:
                heapq.heappush(v2, -heapq.heappop(v1))
            if len(v2) > len(v1):
                heapq.heappush(v1, -heapq.heappop(v2))
            if len(v1) + len(v2) > 2 * a2:
                restore()
            purge(v1, -1)
            purge(v2, 1)
            v6 = float(-v1[0]) if a2 % 2 else (-v1[0] + v2[0]) / 2
            v4.append(v6)
        return v4
