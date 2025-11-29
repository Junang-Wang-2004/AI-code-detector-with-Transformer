class MyQueue:

    def __init__(self):
        self.enq_stack = []
        self.deq_stack = []

    def push(self, x):
        self.enq_stack.append(x)

    def _transfer(self):
        while self.enq_stack:
            self.deq_stack.append(self.enq_stack.pop())

    def peek(self):
        if not self.deq_stack:
            self._transfer()
        return self.deq_stack[-1]

    def pop(self):
        if not self.deq_stack:
            self._transfer()
        return self.deq_stack.pop()

    def empty(self):
        return len(self.enq_stack) == 0 and len(self.deq_stack) == 0
