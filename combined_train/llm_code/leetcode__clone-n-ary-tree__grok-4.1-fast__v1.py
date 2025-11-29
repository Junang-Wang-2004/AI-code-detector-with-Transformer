class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.children = list(a2) if a2 else []

class C2:

    def cloneTree(self, a1):
        if not a1:
            return None
        v1 = []
        v2 = C1(a1.val)
        v1.append([a1, v2, 0])
        while v1:
            v3, v4, v5 = v1[-1]
            if v5 >= len(v3.children):
                v1.pop()
            else:
                v6 = v3.children[v5]
                v7 = C1(v6.val)
                v4.children.append(v7)
                v1[-1][2] += 1
                v1.append([v6, v7, 0])
        return v2
