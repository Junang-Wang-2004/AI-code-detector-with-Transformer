from collections import deque

class C1:

    def longestSubarray(self, a1, a2):
        v1 = deque()
        v2 = deque()
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            while v1 and a1[v1[-1]] <= a1[v5]:
                v1.pop()
            v1.append(v5)
            while v2 and a1[v2[-1]] >= a1[v5]:
                v2.pop()
            v2.append(v5)
            while a1[v1[0]] - a1[v2[0]] > a2:
                if v1[0] == v4:
                    v1.popleft()
                if v2[0] == v4:
                    v2.popleft()
                v4 += 1
            v3 = max(v3, v5 - v4 + 1)
        return v3
