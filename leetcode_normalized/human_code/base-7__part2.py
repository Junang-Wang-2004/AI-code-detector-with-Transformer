class C1(object):

    def convertToBase7(self, a1):
        """
        """
        if a1 < 0:
            return '-' + self.convertToBase7(-a1)
        if a1 < 7:
            return str(a1)
        return self.convertToBase7(a1 // 7) + str(a1 % 7)
