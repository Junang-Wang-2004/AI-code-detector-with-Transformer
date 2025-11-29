from collections import deque

class C1:

    def maxResult(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = [0] * v1
        v2[0] = a1[0]
        v3 = deque([0])
        for v4 in range(1, v1):
            while v3 and v3[0] < v4 - a2:
                v3.popleft()
            v2[v4] = a1[v4] + v2[v3[0]]
            while v3 and v2[v3[-1]] <= v2[v4]:
                v3.pop()
            v3.append(v4)
        return v2[-1]
