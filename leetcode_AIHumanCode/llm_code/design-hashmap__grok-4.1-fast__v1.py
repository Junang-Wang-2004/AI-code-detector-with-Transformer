class MyHashMap:
    def __init__(self):
        self.size = 10007
        self.table = [[] for _ in range(self.size)]

    def _bucket(self, k):
        return k % self.size

    def put(self, k, v):
        b = self._bucket(k)
        for i in range(len(self.table[b])):
            if self.table[b][i][0] == k:
                self.table[b][i] = (k, v)
                return
        self.table[b].append((k, v))

    def get(self, k):
        b = self._bucket(k)
        for pair in self.table[b]:
            if pair[0] == k:
                return pair[1]
        return -1

    def remove(self, k):
        b = self._bucket(k)
        for i in range(len(self.table[b])):
            if self.table[b][i][0] == k:
                del self.table[b][i]
                return
