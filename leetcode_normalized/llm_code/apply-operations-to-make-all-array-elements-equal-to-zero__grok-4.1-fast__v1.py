from collections import deque

class C1(object):

    def checkArray(self, a1, a2):
        v1 = deque()
        v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] < v2:
                return False
            v4 = a1[v3] - v2
            v2 += v4
            v1.append(v4)
            if v3 >= a2 - 1:
                v2 -= v1.popleft()
        return v2 == 0
