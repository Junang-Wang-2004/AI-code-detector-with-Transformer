class C1(object):

    def resultingString(self, a1):
        v1 = []
        for v2 in a1:
            if v1 and (abs(ord(v2) - ord(v1[-1])) == 1 or abs(ord(v2) - ord(v1[-1])) == 25):
                v1.pop()
            else:
                v1.append(v2)
        return ''.join(v1)
