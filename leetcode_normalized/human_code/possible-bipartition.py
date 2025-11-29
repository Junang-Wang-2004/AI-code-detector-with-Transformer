import collections

class C1(object):

    def possibleBipartition(self, a1, a2):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v1[v4 - 1].append(v3 - 1)
        v5 = [0] * a1
        v5[0] = 1
        v6 = collections.deque([0])
        while v6:
            v7 = v6.popleft()
            for v8 in v1[v7]:
                if v5[v8] == v5[v7]:
                    return False
                elif v5[v8] == -v5[v7]:
                    continue
                v5[v8] = -v5[v7]
                v6.append(v8)
        return True
