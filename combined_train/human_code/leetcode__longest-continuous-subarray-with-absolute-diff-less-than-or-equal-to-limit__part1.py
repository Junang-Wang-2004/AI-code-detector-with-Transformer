import collections

class C1(object):

    def longestSubarray(self, a1, a2):
        """
        """
        v1, v2 = (collections.deque(), collections.deque())
        v3 = 0
        for v4, v5 in enumerate(a1):
            while v1 and a1[v1[-1]] <= v5:
                v1.pop()
            v1.append(v4)
            while v2 and a1[v2[-1]] >= v5:
                v2.pop()
            v2.append(v4)
            if a1[v1[0]] - a1[v2[0]] > a2:
                if v1[0] == v3:
                    v1.popleft()
                if v2[0] == v3:
                    v2.popleft()
                v3 += 1
        return len(a1) - v3
