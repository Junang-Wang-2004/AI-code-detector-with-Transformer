class C1:

    def __init__(self, a1):
        self.backward = [a1]
        self.forward = []

    def visit(self, a1):
        self.backward.append(a1)
        self.forward = []

    def back(self, a1):
        while a1 > 0 and len(self.backward) > 1:
            self.forward.append(self.backward.pop())
            a1 -= 1
        return self.backward[-1]

    def forward(self, a1):
        while a1 > 0 and self.forward:
            self.backward.append(self.forward.pop())
            a1 -= 1
        return self.backward[-1]
