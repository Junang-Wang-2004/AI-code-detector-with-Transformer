class C1(object):
    """
    """

    def rotate(self, a1, a2):

        def reverse(a1, a2, a3):
            while a2 < a3:
                a1[a2], a1[a3 - 1] = (a1[a3 - 1], a1[a2])
                a2 += 1
                a3 -= 1
        a2 %= len(a1)
        reverse(a1, 0, len(a1))
        reverse(a1, 0, a2)
        reverse(a1, a2, len(a1))
