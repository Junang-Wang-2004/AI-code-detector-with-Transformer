from collections import deque

class C1(object):

    def maxSlidingWindow(self, a1, a2):
        if not a1:
            return []
        v1 = deque()
        v2 = []
        for v3 in range(a2):
            while v1 and a1[v1[-1]] <= a1[v3]:
                v1.pop()
            v1.append(v3)
        v2.append(a1[v1[0]])
        for v3 in range(a2, len(a1)):
            if v1[0] == v3 - a2:
                v1.popleft()
            while v1 and a1[v1[-1]] <= a1[v3]:
                v1.pop()
            v1.append(v3)
            v2.append(a1[v1[0]])
        return v2
