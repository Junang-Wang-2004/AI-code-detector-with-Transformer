class C1:

    def lowestCommonAncestor(self, a1, a2):
        v1 = []
        v2 = a1
        while v2:
            v1.append(v2)
            v2 = v2.parent
        v3 = []
        v2 = a2
        while v2:
            v3.append(v2)
            v2 = v2.parent
        v4 = len(v1) - 1
        v5 = len(v3) - 1
        while v4 >= 0 and v5 >= 0 and (v1[v4] == v3[v5]):
            v4 -= 1
            v5 -= 1
        return v1[v4 + 1]
