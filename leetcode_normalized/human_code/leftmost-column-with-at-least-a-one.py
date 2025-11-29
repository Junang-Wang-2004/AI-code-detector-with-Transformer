class C1(object):

    def get(self, a1, a2):
        pass

    def dimensions(self):
        pass

class C2(object):

    def leftMostColumnWithOne(self, a1):
        """
        """
        v1, v2 = a1.dimensions()
        v3, v4 = (0, v2 - 1)
        while v3 < v1 and v4 >= 0:
            if not a1.get(v3, v4):
                v3 += 1
            else:
                v4 -= 1
        return v4 + 1 if v4 + 1 != v2 else -1
