class C1(object):

    def kthLuckyNumber(self, a1):
        """
        """
        return bin(a1 + 1)[3:].replace('1', '7').replace('0', '4')
