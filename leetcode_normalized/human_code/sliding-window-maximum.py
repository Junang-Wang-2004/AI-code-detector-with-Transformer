from collections import deque

class C1(object):

    def maxSlidingWindow(self, a1, a2):
        """
        """
        v1, v2 = ([], deque())
        for v3 in range(len(a1)):
            if v2 and v3 - v2[0] == a2:
                v2.popleft()
            while v2 and a1[v2[-1]] <= a1[v3]:
                v2.pop()
            v2.append(v3)
            if v3 >= a2 - 1:
                v1.append(a1[v2[0]])
        return v1
