import collections

class C1(object):

    def findMaximumLength(self, a1):
        """
        """
        v1 = v2 = v3 = v4 = 0
        v5 = collections.deque()
        for v6 in range(len(a1)):
            v2 += a1[v6]
            while v5 and v5[0][0] <= v2:
                v7, v3, v4 = v5.popleft()
            v8, v1 = (v2 - v3, v4 + 1)
            while v5 and v5[-1][0] >= v8 + v2:
                v5.pop()
            v5.append((v8 + v2, v2, v1))
        return v1
