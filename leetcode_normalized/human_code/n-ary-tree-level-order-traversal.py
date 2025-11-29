class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def levelOrder(self, a1):
        """
        """
        if not a1:
            return []
        v1, v2 = ([], [a1])
        while v2:
            v1.append([node.val for v3 in v2])
            v2 = [child for v3 in v2 for v4 in v3.children if v4]
        return v1
