from collections import deque

class C1:

    def maximumScoreAfterOperations(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [[] for v3 in range(v1)]
        v7 = [False] * v1
        v8 = deque([0])
        v7[0] = True
        while v8:
            v9 = v8.popleft()
            for v10 in v2[v9]:
                if not v7[v10]:
                    v7[v10] = True
                    v6[v9].append(v10)
                    v8.append(v10)
        v11 = sum(a2)

        def get_dp(a1):
            if not v6[a1]:
                return a2[a1]
            v1 = sum((get_dp(c) for v2 in v6[a1]))
            return min(v1, a2[a1])
        return v11 - get_dp(0)
