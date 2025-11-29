class C1(object):

    def isValid(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2 == 'c':
                if v1[-2:] == ['a', 'b']:
                    v1.pop()
                    v1.pop()
                else:
                    return False
            else:
                v1.append(v2)
        return not v1
