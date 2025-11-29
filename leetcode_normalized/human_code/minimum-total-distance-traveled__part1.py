import collections

class C1(object):

    def minimumTotalDistance(self, a1, a2):
        """
        """
        (a1.sort(), a2.sort())
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        for v2 in range(len(a2)):
            v3 = 0
            v4 = collections.deque([(v1[0] - v3, 0)])
            for v5 in range(1, len(a1) + 1):
                v3 += abs(a1[v5 - 1] - a2[v2][0])
                if v5 - v4[0][1] == a2[v2][1] + 1:
                    v4.popleft()
                while v4 and v4[-1][0] >= v1[v5] - v3:
                    v4.pop()
                v4.append((v1[v5] - v3, v5))
                v1[v5] = v4[0][0] + v3
        return v1[-1]
