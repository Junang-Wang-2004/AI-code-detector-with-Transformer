class C1:

    def checkRecord(self, a1):
        v1 = 0
        v2 = 0
        for v3 in a1:
            if v3 == 'A':
                v1 += 1
                if v1 > 1:
                    return False
                v2 = 0
            elif v3 == 'L':
                v2 += 1
                if v2 >= 3:
                    return False
            else:
                v2 = 0
        return True
