import collections

class C1(object):

    def findMaxValueOfEquation(self, a1, a2):
        """
        """
        v1 = float('-inf')
        v2 = collections.deque()
        for v3, (v4, v5) in enumerate(a1):
            while v2 and a1[v2[0]][0] < v4 - a2:
                v2.popleft()
            if v2:
                v1 = max(v1, a1[v2[0]][1] - a1[v2[0]][0] + v5 + v4)
            while v2 and a1[v2[-1]][1] - a1[v2[-1]][0] <= v5 - v4:
                v2.pop()
            v2.append(v3)
        return v1
