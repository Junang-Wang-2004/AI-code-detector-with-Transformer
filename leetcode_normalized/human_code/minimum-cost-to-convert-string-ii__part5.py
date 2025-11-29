import itertools
import heapq

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__idxs = []
                self.k = 0
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                self.__idxs.append(-1)
                return len(self.__nodes) - 1

            def add(self, a1):
                v1 = 0
                for v2 in a1:
                    v3 = ord(v2) - ord('a')
                    if self.__nodes[v1][v3] == -1:
                        self.__nodes[v1][v3] = self.__new_node()
                    v1 = self.__nodes[v1][v3]
                if self.__idxs[v1] == -1:
                    self.__idxs[v1] = self.k
                    self.k += 1
                    return (True, self.__idxs[v1])
                return (False, self.__idxs[v1])

            def query(self, a1):
                v1 = 0
                for v2 in a1:
                    v1 = self.__nodes[v1][ord(v2) - ord('a')]
                return self.__idxs[v1]

            def next(self, a1, a2):
                return self.__nodes[a1][ord(a2) - ord('a')]

            def id(self, a1):
                return self.__idxs[a1]
        v2 = Trie()
        for v3 in itertools.chain(a3, a4):
            v2.add(v3)

        def dijkstra(a1):
            v1 = {a1: 0}
            v2 = [(0, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                if v4 not in dist:
                    continue
                for v5, v6 in dist[v4].items():
                    if v5 in v1 and v1[v5] <= v3 + v6:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return v1
        v4 = {}

        def memoization(a1, a2):
            if a1 not in v4:
                v4[a1] = dijkstra(a1)
            return v4[a1][a2] if a2 in v4[a1] else v1
        v5 = {}
        for v6 in range(len(a3)):
            v7, v8 = (v2.query(a3[v6]), v2.query(a4[v6]))
            if v7 not in v5:
                v5[v7] = {v8: v1}
            if v8 not in v5[v7]:
                v5[v7][v8] = v1
            v5[v7][v8] = min(v5[v7][v8], a5[v6])
        v9 = [v1] * (max((len(v3) for v3 in a3)) + 1)
        v9[0] = 0
        for v6 in range(len(a1)):
            if v9[v6 % len(v9)] == v1:
                continue
            if a1[v6] == a2[v6]:
                v9[(v6 + 1) % len(v9)] = min(v9[(v6 + 1) % len(v9)], v9[v6 % len(v9)])
            v7 = v8 = 0
            for v10 in range(v6, len(a1)):
                v7 = v2.next(v7, a1[v10])
                v8 = v2.next(v8, a2[v10])
                if v7 == -1 or v8 == -1:
                    break
                if v2.id(v7) != -1 and v2.id(v8) != -1:
                    v9[(v10 + 1) % len(v9)] = min(v9[(v10 + 1) % len(v9)], v9[v6 % len(v9)] + memoization(v2.id(v7), v2.id(v8)))
            v9[v6 % len(v9)] = v1
        return v9[len(a1) % len(v9)] if v9[len(a1) % len(v9)] != v1 else -1
