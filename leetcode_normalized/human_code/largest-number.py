class C1(object):

    def largestNumber(self, a1):
        a1 = [str(x) for v2 in a1]
        a1.sort(cmp=lambda x, y: cmp(y + v2, v2 + y))
        v3 = ''.join(a1)
        return v3.lstrip('0') or '0'
