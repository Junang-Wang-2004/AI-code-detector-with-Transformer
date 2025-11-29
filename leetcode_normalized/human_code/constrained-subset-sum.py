import collections

class C1(object):

    def constrainedSubsetSum(self, a1, a2):
        """
        """
        v1, v2 = (float('-inf'), collections.deque())
        for v3 in range(len(a1)):
            if v2 and v3 - v2[0][0] == a2 + 1:
                v2.popleft()
            v4 = a1[v3] + (v2[0][1] if v2 else 0)
            while v2 and v2[-1][1] <= v4:
                v2.pop()
            if v4 > 0:
                v2.append((v3, v4))
            v1 = max(v1, v4)
        return v1
