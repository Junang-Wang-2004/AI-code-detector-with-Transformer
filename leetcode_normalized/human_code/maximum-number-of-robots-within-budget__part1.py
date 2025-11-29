import collections

class C1(object):

    def maximumRobots(self, a1, a2, a3):
        """
        """
        v1 = v2 = v3 = 0
        v4 = collections.deque()
        for v5 in range(len(a1)):
            while v4 and a1[v4[-1]] <= a1[v5]:
                v4.pop()
            v4.append(v5)
            v3 += a2[v5]
            if a1[v4[0]] + (v5 - v2 + 1) * v3 > a3:
                if v4[0] == v2:
                    v4.popleft()
                v3 -= a2[v2]
                v2 += 1
        return v5 - v2 + 1
