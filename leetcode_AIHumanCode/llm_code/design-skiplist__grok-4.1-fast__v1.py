import random

MAX_LEVEL = 32

class Node:
    def __init__(self, val):
        self.val = val
        self.next = [None] * MAX_LEVEL

class Skiplist:
    def __init__(self):
        self._sentinel = Node(-float('inf'))
        self._length = 0

    def _locate_predecessors(self, target):
        predecessors = [None] * MAX_LEVEL
        current = self._sentinel
        for level in range(MAX_LEVEL - 1, -1, -1):
            while (current.next[level] is not None and
                   current.next[level].val < target):
                current = current.next[level]
            predecessors[level] = current
        return predecessors

    def _random_height(self):
        height = 1
        while (height < MAX_LEVEL and
               random.randint(1, 2) == 1):
            height += 1
        return height

    def search(self, target):
        predecessors = self._locate_predecessors(target)
        successor = predecessors[0].next[0]
        return (successor is not None and
                successor.val == target)

    def add(self, num):
        height = self._random_height()
        predecessors = self._locate_predecessors(num)
        new_node = Node(num)
        for i in range(height):
            new_node.next[i] = predecessors[i].next[i]
            predecessors[i].next[i] = new_node
        self._length += 1

    def erase(self, num):
        predecessors = self._locate_predecessors(num)
        candidate = predecessors[0].next[0]
        if candidate is None or candidate.val != num:
            return False
        for i in range(MAX_LEVEL):
            if predecessors[i].next[i] == candidate:
                predecessors[i].next[i] = candidate.next[i]
        self._length -= 1
        return True

    def __len__(self):
        return self._length
