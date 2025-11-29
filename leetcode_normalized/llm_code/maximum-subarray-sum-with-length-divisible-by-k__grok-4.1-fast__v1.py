from collections import deque

class C1(object):

    def maxSubarraySum(self, a1, a2):
        v1 = deque([(0, 0)])
        v2 = 0
        v3 = float('-inf')
        for v4 in range(len(a1)):
            v2 += a1[v4]
            v5 = v4 + 1
            while v1 and v1[0][0] < v5 - a2:
                v1.popleft()
            v3 = max(v3, v2 - v1[0][1])
            while v1 and v1[-1][1] >= v2:
                v1.pop()
            v1.append((v5, v2))
        return v3
