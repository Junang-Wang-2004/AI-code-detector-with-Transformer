class C1(object):

    def findMode(self, a1):
        if not a1:
            return []
        self.modes = []
        self.max_count = 0
        self.current_count = 0
        self.previous = None

        def inorder(a1):
            if a1 is None:
                return
            inorder(a1.left)
            if self.previous is None:
                self.current_count = 1
            elif a1.val == self.previous.val:
                self.current_count += 1
            else:
                self.current_count = 1
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [a1.val]
            elif self.current_count == self.max_count:
                self.modes.append(a1.val)
            self.previous = a1
            inorder(a1.right)
        inorder(a1)
        return self.modes
