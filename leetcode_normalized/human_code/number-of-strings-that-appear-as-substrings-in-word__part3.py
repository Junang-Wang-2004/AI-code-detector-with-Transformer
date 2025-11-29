class C1(object):

    def numOfStrings(self, a1, a2):
        return sum((pattern in a2 for v1 in a1))
