import collections

class C1(object):

    def continuousSubarrays(self, a1):
        """
        """
        v1, v2 = (collections.deque(), collections.deque())
        v3 = v4 = 0
        for v5 in range(len(a1)):
            while v1 and a1[v1[-1]] > a1[v5]:
                v1.pop()
            v1.append(v5)
            while v2 and a1[v2[-1]] < a1[v5]:
                v2.pop()
            v2.append(v5)
            while not a1[v5] - a1[v1[0]] <= 2:
                v4 = max(v4, v1.popleft() + 1)
            while not a1[v2[0]] - a1[v5] <= 2:
                v4 = max(v4, v2.popleft() + 1)
            v3 += v5 - v4 + 1
        return v3
