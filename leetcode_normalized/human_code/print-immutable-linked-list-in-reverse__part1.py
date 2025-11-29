import math

class C1(object):

    def printLinkedListInReverse(self, a1):
        """
        """

        def print_nodes(a1, a2):
            v1 = []
            while a1 and len(v1) != a2:
                v1.append(a1)
                a1 = a1.getNext()
            for v3 in reversed(v1):
                v3.printValue()
        v1 = 0
        v2 = a1
        while v2:
            v2 = v2.getNext()
            v1 += 1
        v3 = int(math.ceil(v1 ** 0.5))
        v4 = []
        v1 = 0
        v2 = a1
        while v2:
            if v1 % v3 == 0:
                v4.append(v2)
            v2 = v2.getNext()
            v1 += 1
        for v5 in reversed(v4):
            print_nodes(v5, v3)
