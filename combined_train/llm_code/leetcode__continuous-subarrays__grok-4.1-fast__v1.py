import collections

class C1:

    def continuousSubarrays(self, a1):
        v1 = collections.deque()
        v2 = collections.deque()
        v3 = 0
        v4 = 0
        v5 = len(a1)
        for v6 in range(v5):
            while v1 and a1[v1[-1]] > a1[v6]:
                v1.pop()
            v1.append(v6)
            while v2 and a1[v2[-1]] < a1[v6]:
                v2.pop()
            v2.append(v6)
            while v3 <= v6:
                while v1 and v1[0] < v3:
                    v1.popleft()
                while v2 and v2[0] < v3:
                    v2.popleft()
                if a1[v2[0]] - a1[v1[0]] <= 2:
                    break
                v3 += 1
            v4 += v6 - v3 + 1
        return v4
