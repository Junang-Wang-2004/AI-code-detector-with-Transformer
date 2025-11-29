class C1(object):
    """
    """

    def rotate(self, a1, a2):
        v1 = 0
        v2 = 0
        while v1 < len(a1):
            v3 = v2
            v4 = a1[v3]
            while True:
                v5 = (v3 + a2) % len(a1)
                a1[v5], v4 = (v4, a1[v5])
                v3 = v5
                v1 += 1
                if v2 == v3:
                    break
            v2 += 1
