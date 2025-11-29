class C1(object):

    def isPalindrome(self, a1):
        if a1 < 0:
            return False
        v1, v2 = (a1, 0)
        while v1:
            v2 *= 10
            v2 += v1 % 10
            v1 //= 10
        return a1 == v2
