import collections

class C1(object):

    def findLexSmallestString(self, a1, a2, a3):
        """
        """
        v1, v2, v3 = (collections.deque([a1]), {a1}, a1)
        while v1:
            v4 = v1.popleft()
            if v4 < v3:
                v3 = v4
            v5 = list(v4)
            for v6, v7 in enumerate(v5):
                if v6 % 2:
                    v5[v6] = str((int(v7) + a2) % 10)
            v5 = ''.join(v5)
            if v5 not in v2:
                v2.add(v5)
                v1.append(v5)
            v8 = v4[a3:] + v4[:a3]
            if v8 not in v2:
                v2.add(v8)
                v1.append(v8)
        return v3
