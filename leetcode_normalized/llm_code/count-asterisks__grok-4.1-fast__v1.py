class C1(object):

    def countAsterisks(self, a1):
        v1 = a1.split('|')
        return sum((seg.count('*') for v2 in v1[::2]))
