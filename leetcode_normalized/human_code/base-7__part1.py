class C1(object):

    def convertToBase7(self, a1):
        if a1 < 0:
            return '-' + self.convertToBase7(-a1)
        v1 = ''
        while a1:
            v1 = str(a1 % 7) + v1
            a1 //= 7
        return v1 if v1 else '0'
