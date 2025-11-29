import collections

class C1:

    def minMaxSubarraySum(self, a1, a2):

        def compute_sum(a1):
            v1 = collections.deque()
            v2 = 0
            v3 = 0
            v4 = len(a1)
            for v5 in range(v4):
                v6 = max(v5 - a2 + 1, 0)
                while v1 and (not (a1[v1[-1]] < a1[v5] if a1 else a1[v1[-1]] > a1[v5])):
                    v7 = v1.pop()
                    v8 = v1[-1] + 1 if v1 else v6
                    v9 = v7 - v8 + 1
                    v2 -= v9 * a1[v7]
                v8 = v1[-1] + 1 if v1 else v6
                v9 = v5 - v8 + 1
                v1.append(v5)
                v2 += v9 * a1[v5]
                v3 += v2
                if v5 >= a2 - 1:
                    v10 = v5 - a2 + 1
                    v2 -= a1[v1[0]]
                    if v1[0] == v10:
                        v1.popleft()
            return v3
        return compute_sum(True) + compute_sum(False)
