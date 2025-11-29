class C1(object):

    def validWordAbbreviation(self, a1, a2):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a2:
            if v3.isdigit():
                if v2 == 0 and v3 == '0':
                    return False
                v2 *= 10
                v2 += int(v3)
            else:
                if v2:
                    v1 += v2
                    v2 = 0
                if v1 >= len(a1) or a1[v1] != v3:
                    return False
                v1 += 1
        if v2:
            v1 += v2
        return v1 == len(a1)
