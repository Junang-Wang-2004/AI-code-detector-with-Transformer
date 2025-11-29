import collections

class C1(object):

    def maxCandies(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = 0
        v2 = collections.deque(a5)
        while v2:
            v3 = False
            for v4 in range(len(v2)):
                v5 = v2.popleft()
                if not a1[v5]:
                    v2.append(v5)
                    continue
                v3 = True
                v1 += a2[v5]
                for v6 in a3[v5]:
                    a1[v6] = 1
                for v7 in a4[v5]:
                    v2.append(v7)
            if not v3:
                break
        return v1
