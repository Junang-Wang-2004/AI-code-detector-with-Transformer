import collections

class C1(object):

    def maximumTotalDamage(self, a1):
        """
        """
        v1 = 2
        a1.sort()
        v2 = collections.deque()
        v3 = 0
        for v4 in a1:
            if v2 and v2[-1][0] == v4:
                v2[-1][1] += v4
                continue
            while v2 and v2[0][0] + v1 < v4:
                v3 = max(v3, v2.popleft()[1])
            v2.append([v4, v3 + v4])
        return max((v4 for v5, v4 in v2))
