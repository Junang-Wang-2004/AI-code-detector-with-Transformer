import collections

class C1(object):

    def alienOrder(self, a1):
        """
        """
        v1, v2 = (set(), {})
        for v3 in range(len(a1)):
            for v4 in a1[v3]:
                v1.add(v4)
        for v5 in v1:
            v2[v5] = []
        for v3 in range(1, len(a1)):
            if len(a1[v3 - 1]) > len(a1[v3]) and a1[v3 - 1][:len(a1[v3])] == a1[v3]:
                return ''
            self.findEdges(a1[v3 - 1], a1[v3], v2)
        v6 = []
        v7 = {}
        for v5 in v1:
            if self.topSortDFS(v5, v5, v2, v7, v6):
                return ''
        return ''.join(v6)

    def findEdges(self, a1, a2, a3):
        v1 = min(len(a1), len(a2))
        for v2 in range(v1):
            if a1[v2] != a2[v2]:
                a3[a2[v2]].append(a1[v2])
                break

    def topSortDFS(self, a1, a2, a3, a4, a5):
        if a2 not in a4:
            a4[a2] = a1
            for v1 in a3[a2]:
                if self.topSortDFS(a1, v1, a3, a4, a5):
                    return True
            a5.append(a2)
        elif a4[a2] == a1:
            return True
        return False
