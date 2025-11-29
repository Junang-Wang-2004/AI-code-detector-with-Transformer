class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def minimumOperations(self, a1):
        """
        """
        v1 = 0
        v2 = [a1]
        while v2:
            v3 = []
            for v4 in v2:
                if v4.left:
                    v3.append(v4.left)
                if v4.right:
                    v3.append(v4.right)
            v5 = list(range(len(v2)))
            v5.sort(key=lambda x: v2[x].val)
            for v6 in range(len(v2)):
                while v5[v6] != v6:
                    v5[v5[v6]], v5[v6] = (v5[v6], v5[v5[v6]])
                    v1 += 1
            v2 = v3
        return v1
