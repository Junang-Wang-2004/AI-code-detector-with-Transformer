class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def postorder(self, a1):
        """
        """
        if not a1:
            return []
        v1, v2 = ([], [a1])
        while v2:
            v3 = v2.pop()
            v1.append(v3.val)
            for v4 in v3.children:
                if v4:
                    v2.append(v4)
        return v1[::-1]
