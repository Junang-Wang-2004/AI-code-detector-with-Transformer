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
        if not a1:
            return True
        v1 = []
        v2 = a1
        while v2:
            v1.append(v2.val)
            v2 = v2.next
        v3 = len(v1)
        v4 = [0] * v3
        v5 = 0
        v6 = 1
        while v6 < v3:
            if v1[v6] == v1[v5]:
                v5 += 1
                v4[v6] = v5
                v6 += 1
            elif v5 != 0:
                v5 = v4[v5 - 1]
            else:
                v4[v6] = 0
                v6 += 1

        def search(a1, a2):
            if not a1:
                return False
            while a2 < v3 and v1[a2] != a1.val:
                if a2 == 0:
                    break
                a2 = v4[a2 - 1]
            if a2 < v3 and v1[a2] == a1.val:
                a2 += 1
            if a2 == v3:
                return True
            return search(a1.left, a2) or search(a1.right, a2)
        return search(a2, 0)
