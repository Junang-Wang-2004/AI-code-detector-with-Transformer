import collections
import heapq

class C1(object):

    def minNumberOfSemesters(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3):
            if a3[a2] == -1:
                a3[a2] = max((dfs(a1, child, a3) for v1 in a1[a2])) + 1 if a2 in a1 else 1
            return a3[a2]
        v1 = [0] * a1
        v2 = collections.defaultdict(list)
        for v3, v4 in a2:
            v2[v3 - 1].append(v4 - 1)
            v1[v4 - 1] += 1
        v5 = [-1] * a1
        for v6 in range(a1):
            dfs(v2, v6, v5)
        v7 = []
        for v6 in range(a1):
            if not v1[v6]:
                heapq.heappush(v7, (-v5[v6], v6))
        v8 = 0
        while v7:
            v9 = []
            for v10 in range(min(len(v7), a3)):
                v10, v11 = heapq.heappop(v7)
                if v11 not in v2:
                    continue
                for v12 in v2[v11]:
                    v1[v12] -= 1
                    if not v1[v12]:
                        v9.append(v12)
            v8 += 1
            for v11 in v9:
                heapq.heappush(v7, (-v5[v11], v11))
        return v8
