class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def str2tree(self, a1):
        """
        """

        def str2treeHelper(a1, a2):
            v1 = a2
            if a1[a2] == '-':
                a2 += 1
            while a2 < len(a1) and a1[a2].isdigit():
                a2 += 1
            v3 = C1(int(a1[v1:a2]))
            if a2 < len(a1) and a1[a2] == '(':
                a2 += 1
                v3.left, a2 = str2treeHelper(a1, a2)
                a2 += 1
            if a2 < len(a1) and a1[a2] == '(':
                a2 += 1
                v3.right, a2 = str2treeHelper(a1, a2)
                a2 += 1
            return (v3, a2)
        return str2treeHelper(a1, 0)[0] if a1 else None
