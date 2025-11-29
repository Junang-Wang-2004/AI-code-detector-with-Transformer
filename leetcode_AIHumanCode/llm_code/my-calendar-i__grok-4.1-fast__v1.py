class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.lchild = None
        self.rchild = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        node = Node(start, end)
        current = self.root
        while True:
            if start >= current.e:
                if current.rchild is None:
                    current.rchild = node
                    return True
                current = current.rchild
            elif end <= current.s:
                if current.lchild is None:
                    current.lchild = node
                    return True
                current = current.lchild
            else:
                return False
