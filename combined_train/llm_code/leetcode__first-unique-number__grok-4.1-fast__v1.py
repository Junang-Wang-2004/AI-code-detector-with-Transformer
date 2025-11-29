class C1:

    def __init__(self, a1):
        self._head = {'prev': None, 'next': None}
        self._tail = {'prev': None, 'next': None}
        self._head['next'] = self._tail
        self._tail['prev'] = self._head
        self._val_to_node = {}
        self._duplicates = set()
        for v1 in a1:
            self.add(v1)

    def add(self, a1):
        if a1 in self._duplicates:
            return
        if a1 in self._val_to_node:
            v1 = self._val_to_node[a1]
            v1['prev']['next'] = v1['next']
            v1['next']['prev'] = v1['prev']
            del self._val_to_node[a1]
            self._duplicates.add(a1)
        else:
            v2 = {'val': a1, 'prev': self._tail['prev'], 'next': self._tail}
            self._tail['prev']['next'] = v2
            self._tail['prev'] = v2
            self._val_to_node[a1] = v2

    def showFirstUnique(self):
        if self._head['next'] == self._tail:
            return -1
        return self._head['next']['val']
