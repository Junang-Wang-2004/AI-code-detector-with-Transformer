class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def postorder(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = [(a1, 0)]
        while v2:
            v3, v4 = v2[-1]
            if v4 < len(v3.children):
                v2[-1] = (v3, v4 + 1)
                v5 = v3.children[v4]
                if v5:
                    v2.append((v5, 0))
            else:
                v1.append(v3.val)
                v2.pop()
        return v1
