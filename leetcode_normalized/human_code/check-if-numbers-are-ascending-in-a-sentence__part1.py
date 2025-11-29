class C1(object):

    def areNumbersAscending(self, a1):
        """
        """
        v1 = v2 = -1
        for v3, v4 in enumerate(a1):
            if v4.isdigit():
                v2 = max(v2, 0) * 10 + int(v4)
                continue
            if v1 != -1 and v2 != -1 and (v1 >= v2):
                return False
            if v2 != -1:
                v1 = v2
            v2 = -1
        return v2 == -1 or v1 < v2
