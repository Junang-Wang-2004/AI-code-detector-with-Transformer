import abc
from abc import ABCMeta, abstractmethod

class C1(metaclass=ABCMeta):

    @abstractmethod
    def evaluate(self):
        pass
import operator

class C2(C1):
    v1 = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

    def evaluate(self):
        v1 = [0]
        v2 = [(1, (self, v1))]
        while v2:
            v3, v4 = v2.pop()
            if v3 == 1:
                v5, v6 = v4
                if v5.val.isdigit():
                    v6[0] = int(v5.val)
                    continue
                v7, v8 = ([0], [0])
                v2.append((2, (v5, v7, v8, v6)))
                v2.append((1, (v5.right, v8)))
                v2.append((1, (v5.left, v7)))
            elif v3 == 2:
                v5, v7, v8, v6 = v4
                v6[0] = C2.ops[v5.val](v7[0], v8[0])
        return v1[0]

class C3(object):

    def buildTree(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2.isdigit():
                v1.append(C2(v2))
            else:
                v3 = C2(v2)
                v3.right = v1.pop()
                v3.left = v1.pop()
                v1.append(v3)
        return v1.pop()
