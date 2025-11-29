class C1(object):

    def isPalindrome(self, a1):
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2:
            while v1 < v2 and (not a1[v1].isalnum()):
                v1 += 1
            while v1 < v2 and (not a1[v2].isalnum()):
                v2 -= 1
            if a1[v1].lower() != a1[v2].lower():
                return False
            v1, v2 = (v1 + 1, v2 - 1)
        return True
