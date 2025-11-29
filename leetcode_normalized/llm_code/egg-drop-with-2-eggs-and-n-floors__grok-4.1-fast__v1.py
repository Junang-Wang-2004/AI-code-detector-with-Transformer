class C1(object):

    def twoEggDrop(self, a1):
        v1, v2 = (0, a1)
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if v3 * (v3 + 1) // 2 >= a1:
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
