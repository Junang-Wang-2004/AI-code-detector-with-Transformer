import collections

class C1:

    def __init__(self, a1, a2):
        v1 = ord(a2) - ord('A') + 1
        self.cells = [[0] * v1 for v2 in range(a1 + 1)]
        self.outgoing = collections.defaultdict(lambda: collections.defaultdict(int))
        self.incoming = collections.defaultdict(set)

    def set(self, a1, a2, a3):
        v1 = ord(a2) - ord('A')
        self._unlink(a1, v1)
        v2 = self.cells[a1][v1]
        self.cells[a1][v1] = a3
        self._ripple(a1, v1, a3 - v2)

    def get(self, a1, a2):
        return self.cells[a1][ord(a2) - ord('A')]

    def sum(self, a1, a2, a3):
        v1 = ord(a2) - ord('A')
        self._unlink(a1, v1)
        v2 = 0
        v3 = set()
        for v4 in a3:
            v5 = v4.split(':')
            v6 = v5[0]
            v7 = v5[1] if len(v5) > 1 else v6
            v8 = ord(v6[0]) - ord('A')
            v9 = int(v6[1:])
            v10 = ord(v7[0]) - ord('A')
            v11 = int(v7[1:])
            for v12 in range(v9, v11 + 1):
                for v13 in range(v8, v10 + 1):
                    v2 += self.cells[v12][v13]
                    v14 = (v12, v13)
                    self.outgoing[v14][a1, v1] += 1
                    v3.add(v14)
        self.incoming[a1, v1] = v3
        v15 = self.cells[a1][v1]
        self.cells[a1][v1] = v2
        self._ripple(a1, v1, v2 - v15)
        return v2

    def _unlink(self, a1, a2):
        v1 = self.incoming[a1, a2]
        for v2, v3 in v1:
            self.outgoing[v2, v3].pop((a1, a2), None)
        self.incoming[a1, a2].clear()

    def _ripple(self, a1, a2, a3):
        if not a3:
            return
        v1 = collections.deque([((a1, a2), a3)])
        while v1:
            v2, v3 = v1.popleft()
            for v4, v5 in self.outgoing[v2].items():
                v6 = v3 * v5
                v7, v8 = v4
                self.cells[v7][v8] += v6
                v1.append((v4, v6))
