import collections

class C1(object):

    def maxResult(self, a1, a2):
        """
        """
        v1 = 0
        v2 = collections.deque()
        for v3, v4 in enumerate(a1):
            if v2 and v2[0][0] == v3 - a2 - 1:
                v2.popleft()
            v1 = v4 if not v2 else v2[0][1] + v4
            while v2 and v2[-1][1] <= v1:
                v2.pop()
            v2.append((v3, v1))
        return v1
