class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def levelOrder(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = [a1]
        while v2:
            v3 = []
            v4 = len(v2)
            for v5 in range(v4):
                v6 = v2.pop(0)
                v3.append(v6.val)
                for v7 in v6.children:
                    if v7:
                        v2.append(v7)
            v1.append(v3)
        return v1
