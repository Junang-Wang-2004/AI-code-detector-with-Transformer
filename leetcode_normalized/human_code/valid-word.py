class C1(object):

    def isValid(self, a1):
        """
        """
        v1 = 'aeiou'
        if len(a1) < 3:
            return False
        v2 = v3 = False
        for v4 in a1:
            if v4.isalpha():
                if v4.lower() in v1:
                    v2 = True
                else:
                    v3 = True
            elif not v4.isdigit():
                return False
        return v2 and v3
