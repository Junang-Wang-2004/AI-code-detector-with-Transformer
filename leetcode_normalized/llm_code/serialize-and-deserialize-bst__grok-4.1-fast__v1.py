class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def serialize(self, a1):
        if not a1:
            return ''
        v1 = [a1]
        v2 = []
        while v1:
            v3 = v1.pop()
            if v3:
                v2.append(str(v3.val))
                v1.append(v3.right)
                v1.append(v3.left)
        return ' '.join(v2)

    def deserialize(self, a1):
        v1 = [int(x) for v2 in a1.split()]
        v3 = 0

        def build(a1, a2):
            nonlocal idx
            if v3 >= len(v1) or not a1 < v1[v3] < a2:
                return None
            v1 = v1[v3]
            v2 += 1
            v3 = C1(v1)
            v3.left = build(a1, v1)
            v3.right = build(v1, a2)
            return v3
        return build(float('-inf'), float('inf'))
