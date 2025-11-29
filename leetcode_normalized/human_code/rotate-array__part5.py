class C1(object):
    """
    """

    def rotate(self, a1, a2):
        while a2 > 0:
            a1.insert(0, a1.pop())
            a2 -= 1
