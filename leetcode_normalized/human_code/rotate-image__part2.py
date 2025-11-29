class C1(object):

    def rotate(self, a1):
        return [list(reversed(x)) for v1 in zip(*a1)]
