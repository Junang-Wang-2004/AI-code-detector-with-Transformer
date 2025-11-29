class C1:

    def __init__(self, a1, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def nextLargerNodes(self, a1):
        v1 = []
        v2 = a1
        while v2:
            v1.append(v2.val)
            v2 = v2.next
        v3 = len(v1)
        v4 = [0] * v3
        v5 = []
        for v6 in range(v3 - 1, -1, -1):
            while v5 and v5[-1] <= v1[v6]:
                v5.pop()
            if v5:
                v4[v6] = v5[-1]
            v5.append(v1[v6])
        return v4
