class C1(object):

    def isPowerOfFour(self, a1):
        """
        """
        while a1 and (not a1 & 3):
            a1 >>= 2
        return a1 == 1

class C2(object):

    def isPowerOfFour(self, a1):
        """
        """
        a1 = bin(a1)
        return True if a1[2:].startswith('1') and len(a1[2:]) == a1.count('0') and a1.count('0') % 2 and ('-' not in a1) else False
