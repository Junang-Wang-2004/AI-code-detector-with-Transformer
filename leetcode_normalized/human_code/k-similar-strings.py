import collections

class C1(object):

    def kSimilarity(self, a1, a2):
        """
        """

        def neighbors(a1, a2):
            for v1, v2 in enumerate(a1):
                if v2 != a2[v1]:
                    break
            v3 = list(a1)
            for v4 in range(v1 + 1, len(a1)):
                if v3[v4] == a2[v1]:
                    v3[v1], v3[v4] = (v3[v4], v3[v1])
                    yield ''.join(v3)
                    v3[v4], v3[v1] = (v3[v1], v3[v4])
        v1 = collections.deque([a1])
        v2 = set()
        v3 = 0
        while v1:
            for v4 in range(len(v1)):
                v5 = v1.popleft()
                if v5 == a2:
                    return v3
                for v6 in neighbors(v5, a2):
                    if v6 not in v2:
                        v2.add(v6)
                        v1.append(v6)
            v3 += 1
