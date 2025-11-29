import collections

class C1:

    def shortestSubarray(self, a1, a2):
        v1 = [0]
        for v2 in a1:
            v1.append(v1[-1] + v2)
        v3 = float('inf')
        v4 = collections.deque()
        for v5 in range(len(v1)):
            while v4 and v1[v4[-1]] >= v1[v5]:
                v4.pop()
            while v4 and v1[v5] - v1[v4[0]] >= a2:
                v3 = min(v3, v5 - v4.popleft())
            v4.append(v5)
        return v3 if v3 < float('inf') else -1
