class C1(object):

    def rotateTheBox(self, a1):
        return [list(row) for v1 in zip(*a1[::-1])]
