class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = self.right = None

class C2(object):

    def str2tree(self, a1):
        if not a1:
            return None
        v1 = 0

        def build():
            nonlocal idx
            v1 = -1 if a1[v1] == '-' else 1
            if v1 == -1:
                v2 += 1
            v3 = 0
            while v2 < len(a1) and a1[v2].isdigit():
                v3 = v3 * 10 + int(a1[v2])
                v2 += 1
            v4 = C1(v1 * v3)
            if v2 < len(a1) and a1[v2] == '(':
                v2 += 1
                v4.left = build()
                v2 += 1
            if v2 < len(a1) and a1[v2] == '(':
                v2 += 1
                v4.right = build()
                v2 += 1
            return v4
        return build()
