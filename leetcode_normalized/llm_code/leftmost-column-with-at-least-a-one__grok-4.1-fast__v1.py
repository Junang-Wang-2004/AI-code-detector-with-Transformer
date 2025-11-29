class C1(object):

    def leftMostColumnWithOne(self, a1):
        v1, v2 = a1.dimensions()
        v3 = v2
        v4 = 0
        v5 = v2 - 1
        while v4 < v1 and v5 >= 0:
            if a1.get(v4, v5):
                v3 = min(v3, v5)
                v5 -= 1
            else:
                v4 += 1
        return v3 if v3 < v2 else -1
