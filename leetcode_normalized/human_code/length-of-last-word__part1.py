class C1(object):

    def lengthOfLastWord(self, a1):
        v1 = 0
        for v2 in reversed(a1):
            if v2 == ' ':
                if v1:
                    break
            else:
                v1 += 1
        return v1
