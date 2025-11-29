class C1(object):

    def removeElement(self, a1, a2):
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            if a1[v1] == a2:
                a1[v1], a1[v2] = (a1[v2], a1[v1])
                v2 -= 1
            else:
                v1 += 1
        return v2 + 1
