class FirstUnique:

    def __init__(self, nums):
        self._head = {'prev': None, 'next': None}
        self._tail = {'prev': None, 'next': None}
        self._head['next'] = self._tail
        self._tail['prev'] = self._head
        self._val_to_node = {}
        self._duplicates = set()
        for num in nums:
            self.add(num)

    def add(self, value):
        if value in self._duplicates:
            return
        if value in self._val_to_node:
            node = self._val_to_node[value]
            node['prev']['next'] = node['next']
            node['next']['prev'] = node['prev']
            del self._val_to_node[value]
            self._duplicates.add(value)
        else:
            new_node = {'val': value, 'prev': self._tail['prev'], 'next': self._tail}
            self._tail['prev']['next'] = new_node
            self._tail['prev'] = new_node
            self._val_to_node[value] = new_node

    def showFirstUnique(self):
        if self._head['next'] == self._tail:
            return -1
        return self._head['next']['val']
