class C1(object):

    def closestKValues(self, a1, a2, a3):
        """
        """

        class BSTIterator:

            def __init__(self, a1, a2, a3):
                self.stack = list(a1)
                self.cur = self.stack.pop()
                self.child1 = a2
                self.child2 = a3

            def __next__(self):
                v1 = None
                if self.cur and self.child1(self.cur):
                    self.stack.append(self.cur)
                    v1 = self.child1(self.cur)
                    while self.child2(v1):
                        self.stack.append(v1)
                        v1 = self.child2(v1)
                elif self.stack:
                    v2 = self.cur
                    v1 = self.stack.pop()
                    while v1:
                        if self.child2(v1) is v2:
                            break
                        else:
                            v2 = v1
                            v1 = self.stack.pop() if self.stack else None
                self.cur = v1
                return v1
        v1 = []
        while a1:
            v1.append(a1)
            a1 = a1.left if a2 < a1.val else a1.right
        v3 = lambda node: abs(node.val - a2) if node else float('inf')
        v1 = v1[:v1.index(min(v1, key=v3)) + 1]
        v4 = lambda node: node.left
        v5 = lambda node: node.right
        v6, v7 = (BSTIterator(v1, v4, v5), BSTIterator(v1, v5, v4))
        v8, v9 = (next(v6), next(v7))
        v10 = [v1[-1].val]
        for v11 in range(a3 - 1):
            if v3(v8) < v3(v9):
                v10.append(v8.val)
                v8 = next(v6)
            else:
                v10.append(v9.val)
                v9 = next(v7)
        return v10
