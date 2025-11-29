import collections
import heapq

class C1(object):

    def avoidFlood(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        v2 = len(a1) - 1
        for v3 in reversed(a1):
            v1[v3].append(v2)
            v2 -= 1
        v4, v5 = ([], [])
        for v2, v3 in enumerate(a1):
            if v3:
                if len(v1[v3]) >= 2:
                    v1[v3].pop()
                    heapq.heappush(v5, v1[v3][-1])
                v4.append(-1)
            elif v5:
                v6 = heapq.heappop(v5)
                if v6 < v2:
                    return []
                v4.append(a1[v6])
            else:
                v4.append(1)
        return v4 if not v5 else []
