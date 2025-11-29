class OrderedStream:

    def __init__(self, n):
        self.ptr = 0
        self.data = [None] * n

    def insert(self, id_key, val):
        id_key -= 1
        self.data[id_key] = val
        res = []
        while self.ptr < len(self.data) and self.data[self.ptr] is not None:
            res.append(self.data[self.ptr])
            self.ptr += 1
        return res
