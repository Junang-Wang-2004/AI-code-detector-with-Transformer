import collections
import itertools
import operator

def f1(a1):
    v1 = [k for v2, v3 in a1.items() if v3 == 0]
    for v2 in v1:
        a1.pop(v2)

class C1(collections.Counter):

    def __init__(self, a1=None):
        if a1 is None:
            return
        if a1.isdigit():
            if int(a1):
                self.update({(): int(a1)})
        else:
            self[a1,] += 1

    def __add__(self, a1):
        v1 = C1()
        v1.update(self)
        v1.update(a1)
        f1(v1)
        return v1

    def __sub__(self, a1):
        v1 = C1()
        v1.update(self)
        v1.update({k: -v for v2, v3 in a1.items()})
        f1(v1)
        return v1

    def __mul__(self, a1):

        def merge(a1, a2):
            v1 = []
            v2, v3 = (0, 0)
            while v2 != len(a1) or v3 != len(a2):
                if v3 == len(a2) or (v2 != len(a1) and a1[v2] < a2[v3]):
                    v1.append(a1[v2])
                    v2 += 1
                else:
                    v1.append(a2[v3])
                    v3 += 1
            return v1
        v1 = C1()
        for v2, v3 in self.items():
            for v4, v5 in a1.items():
                v1.update({tuple(merge(v2, v4)): v3 * v5})
        f1(v1)
        return v1

    def eval(self, a1):
        v1 = C1()
        for v2, v3 in self.items():
            v4 = []
            for v5 in v2:
                if v5 in a1:
                    v3 *= a1[v5]
                else:
                    v4.append(v5)
            v1[tuple(v4)] += v3
        f1(v1)
        return v1

    def to_list(self):
        return ['*'.join((str(v),) + k) for v1, v2 in sorted(iter(self.items()), key=lambda x: (-len(x[0]), x[0]))]

class C2(object):

    def basicCalculatorIV(self, a1, a2, a3):
        """
        """
        v1 = {'+': operator.add, '-': operator.sub, '*': operator.mul}

        def compute(a1, a2):
            v1, v2 = (a1.pop(), a1.pop())
            a1.append(v1[a2.pop()](v2, v1))

        def parse(a1):
            v1 = {'+': 0, '-': 0, '*': 1}
            v2, v3, v4 = ([], [], [])
            for v5 in range(len(a1)):
                if a1[v5].isalnum():
                    v4.append(a1[v5])
                    if v5 == len(a1) - 1 or not a1[v5 + 1].isalnum():
                        v2.append(C1(''.join(v4)))
                        v4 = []
                elif a1[v5] == '(':
                    v3.append(a1[v5])
                elif a1[v5] == ')':
                    while v3[-1] != '(':
                        compute(v2, v3)
                    v3.pop()
                elif a1[v5] in v1:
                    while v3 and v3[-1] in v1 and (v1[v3[-1]] >= v1[a1[v5]]):
                        compute(v2, v3)
                    v3.append(a1[v5])
            while v3:
                compute(v2, v3)
            return v2[-1]
        v2 = dict(zip(a2, a3))
        return parse(a1).eval(v2).to_list()
