import collections

class C1(object):

    def canReach(self, a1, a2, a3):
        """
        """
        v1 = collections.deque([0])
        v2 = 0
        while v1:
            v3 = v1.popleft()
            for v4 in range(max(v3 + a2, v2 + 1), min(v3 + a3 + 1, len(a1))):
                if a1[v4] != '0':
                    continue
                v1.append(v4)
            v2 = v3 + a3
        return v3 == len(a1) - 1
