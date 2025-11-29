import collections

class C1(object):

    def alienOrder(self, a1):
        """
        """
        v1, v2, v3 = ([], {}, {})
        v4 = collections.deque()
        v5 = set()
        for v6 in a1:
            for v7 in v6:
                v5.add(v7)
        for v8 in range(1, len(a1)):
            if len(a1[v8 - 1]) > len(a1[v8]) and a1[v8 - 1][:len(a1[v8])] == a1[v8]:
                return ''
            self.findEdges(a1[v8 - 1], a1[v8], v2, v3)
        for v9 in v5:
            if v9 not in v2:
                v4.append(v9)
        while v4:
            v10 = v4.popleft()
            v1.append(v10)
            if v10 in v3:
                for v7 in v3[v10]:
                    v2[v7].discard(v10)
                    if not v2[v7]:
                        v4.append(v7)
                del v3[v10]
        if v3:
            return ''
        return ''.join(v1)

    def findEdges(self, a1, a2, a3, a4):
        v1 = min(len(a1), len(a2))
        for v2 in range(v1):
            if a1[v2] != a2[v2]:
                if a2[v2] not in a3:
                    a3[a2[v2]] = set()
                if a1[v2] not in a4:
                    a4[a1[v2]] = set()
                a3[a2[v2]].add(a1[v2])
                a4[a1[v2]].add(a2[v2])
                break
