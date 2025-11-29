class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self._left = Node(0)
        self._right = Node(0)
        self._left.next = self._right
        self._right.prev = self._left
        self._size = 0

    def _find(self, idx):
        if idx <= self._size // 2:
            curr = self._left.next
            for _ in range(idx):
                curr = curr.next
            return curr
        curr = self._right.prev
        for _ in range(self._size - 1 - idx):
            curr = curr.prev
        return curr

    def get(self, index):
        if index < 0 or index >= self._size:
            return -1
        return self._find(index).val

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self._left.next
        new_node.prev = self._left
        self._left.next.prev = new_node
        self._left.next = new_node
        self._size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        new_node.prev = self._right.prev
        new_node.next = self._right
        self._right.prev.next = new_node
        self._right.prev = new_node
        self._size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self._size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self._size:
            self.addAtTail(val)
            return
        target = self._find(index)
        new_node = Node(val)
        new_node.prev = target.prev
        new_node.next = target
        target.prev.next = new_node
        target.prev = new_node
        self._size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self._size:
            return
        node = self._find(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
