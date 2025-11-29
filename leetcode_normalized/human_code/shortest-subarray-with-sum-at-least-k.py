import collections

class C1(object):

    def shortestSubarray(self, a1, a2):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = float('inf')
        v4 = collections.deque()
        for v2, v5 in enumerate(v1):
            while v4 and v5 <= v1[v4[-1]]:
                v4.pop()
            while v4 and v5 - v1[v4[0]] >= a2:
                v3 = min(v3, v2 - v4.popleft())
            v4.append(v2)
        return v3 if v3 != float('inf') else -1
