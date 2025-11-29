from abc import ABC, abstractmethod

class C1(ABC):

    @abstractmethod
    def evaluate(self) -> int:
        pass

class C2(C1):

    def __init__(self, a1):
        self.token = a1
        self.left = None
        self.right = None

    def evaluate(self) -> int:
        if self.token.isdigit():
            return int(self.token)
        v1 = self.left.evaluate()
        v2 = self.right.evaluate()
        if self.token == '+':
            return v1 + v2
        elif self.token == '-':
            return v1 - v2
        elif self.token == '*':
            return v1 * v2
        elif self.token == '/':
            return v1 // v2

class C3:

    def buildTree(self, a1):
        v1 = []
        for v2 in a1:
            if v2.isdigit():
                v3 = C2(v2)
                v1.append(v3)
            else:
                v4 = C2(v2)
                v4.right = v1.pop()
                v4.left = v1.pop()
                v1.append(v4)
        return v1.pop()
