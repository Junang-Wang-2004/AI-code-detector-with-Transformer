class C1:

    def removeElement(self, a1, a2):
        v1 = 0
        for v2 in a1:
            if v2 != a2:
                a1[v1] = v2
                v1 += 1
        return v1
