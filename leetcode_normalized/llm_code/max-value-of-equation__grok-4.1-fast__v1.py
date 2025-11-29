import collections

class C1(object):

    def findMaxValueOfEquation(self, a1, a2):
        v1 = float('-inf')
        v2 = collections.deque()
        v3 = len(a1)
        for v4 in range(v3):
            v5 = a1[v4][0]
            v6 = a1[v4][1]
            while v2 and a1[v2[0]][0] < v5 - a2:
                v2.popleft()
            if v2:
                v7 = v2[0]
                v1 = max(v1, a1[v7][1] - a1[v7][0] + v6 + v5)
            v8 = v6 - v5
            while v2 and a1[v2[-1]][1] - a1[v2[-1]][0] <= v8:
                v2.pop()
            v2.append(v4)
        return v1
