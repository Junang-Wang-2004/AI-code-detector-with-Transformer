class C1(object):

    def findTheDifference(self, a1, a2):
        return chr(sum((ord(ch) for v1 in a2)) - sum((ord(v1) for v1 in a1)))
