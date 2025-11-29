from collections import deque

class C1:

    def minCost(self, a1, a2):
        v1 = len(a1)

        def get_cost(a1):
            v1 = a1 + 1
            v2 = a2 * a1
            v3 = deque()
            for v4 in range(v1 + v1 - 1):
                v5 = v4 % v1
                if v3 and v4 - v3[0] == v1:
                    v3.popleft()
                while v3 and a1[v3[-1] % v1] >= a1[v5]:
                    v3.pop()
                v3.append(v4)
                if v4 >= v1 - 1:
                    v2 += a1[v3[0] % v1]
            return v2
        v2 = 0
        v3 = v1
        while v3 - v2 > 2:
            v4 = v2 + (v3 - v2) // 3
            v5 = v3 - (v3 - v2) // 3
            if get_cost(v4) <= get_cost(v5):
                v3 = v5
            else:
                v2 = v4
        v6 = float('inf')
        for v7 in range(v2, v3 + 1):
            v6 = min(v6, get_cost(v7))
        return v6
