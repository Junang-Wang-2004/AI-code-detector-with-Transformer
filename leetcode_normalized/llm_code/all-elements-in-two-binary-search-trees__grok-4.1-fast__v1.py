class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def getAllElements(self, a1, a2):

        def collect(a1, a2):
            if a1:
                collect(a1.left, a2)
                a2.append(a1.val)
                collect(a1.right, a2)
        v1, v2 = ([], [])
        collect(a1, v1)
        collect(a2, v2)
        v3 = []
        v4, v5 = (0, 0)
        while v4 < len(v1) and v5 < len(v2):
            if v1[v4] <= v2[v5]:
                v3.append(v1[v4])
                v4 += 1
            else:
                v3.append(v2[v5])
                v5 += 1
        v3.extend(v1[v4:])
        v3.extend(v2[v5:])
        return v3
