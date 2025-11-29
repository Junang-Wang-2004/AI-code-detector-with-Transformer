import collections

class C1(object):

    def minimumCoins(self, a1):
        """
        """
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        v2 = collections.deque()
        v3 = 0
        for v4 in range(len(a1)):
            while v2 and v1[v2[-1]] + a1[v2[-1]] >= v1[v4] + a1[v4]:
                v2.pop()
            v2.append(v4)
            while v3 + (v3 + 1) < v4:
                assert len(v2) != 0
                if v2[0] == v3:
                    v2.popleft()
                v3 += 1
            v1[v4 + 1] = v1[v2[0]] + a1[v2[0]]
        return v1[-1]
