class C1(object):

    def kthLargestNumber(self, a1, a2):
        v1 = sorted(a1, key=lambda s: (len(s), s), reverse=True)
        return v1[a2 - 1]
