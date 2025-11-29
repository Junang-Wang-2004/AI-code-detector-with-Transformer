class C1:

    def __init__(self):
        self.size = 10007
        self.table = [[] for v1 in range(self.size)]

    def _bucket(self, a1):
        return a1 % self.size

    def put(self, a1, a2):
        v1 = self._bucket(a1)
        for v2 in range(len(self.table[v1])):
            if self.table[v1][v2][0] == a1:
                self.table[v1][v2] = (a1, a2)
                return
        self.table[v1].append((a1, a2))

    def get(self, a1):
        v1 = self._bucket(a1)
        for v2 in self.table[v1]:
            if v2[0] == a1:
                return v2[1]
        return -1

    def remove(self, a1):
        v1 = self._bucket(a1)
        for v2 in range(len(self.table[v1])):
            if self.table[v1][v2][0] == a1:
                del self.table[v1][v2]
                return
