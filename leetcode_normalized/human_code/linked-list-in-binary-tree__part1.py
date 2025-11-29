class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C3(object):

    def isSubPath(self, a1, a2):
        """
        """

        def getPrefix(a1):
            v1, v2 = ([a1.val], [-1])
            v3 = -1
            v4 = a1.__next__
            while v4:
                while v3 + 1 and v1[v3 + 1] != v4.val:
                    v3 = v2[v3]
                if v1[v3 + 1] == v4.val:
                    v3 += 1
                v1.append(v4.val)
                v2.append(v3)
                v4 = v4.__next__
            return (v1, v2)

        def dfs(a1, a2, a3, a4):
            if not a3:
                return False
            while a4 + 1 and a1[a4 + 1] != a3.val:
                a4 = a2[a4]
            if a1[a4 + 1] == a3.val:
                a4 += 1
            if a4 + 1 == len(a1):
                return True
            return dfs(a1, a2, a3.left, a4) or dfs(a1, a2, a3.right, a4)
        if not a1:
            return True
        v1, v2 = getPrefix(a1)
        return dfs(v1, v2, a2, -1)
