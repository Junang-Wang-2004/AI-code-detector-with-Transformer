class C1:

    def lemonadeChange(self, a1):
        v1 = {5: 0, 10: 0}
        for v2 in a1:
            if v2 == 5:
                v1[5] += 1
            elif v2 == 10:
                if v1[5] == 0:
                    return False
                v1[5] -= 1
                v1[10] += 1
            else:
                v3 = False
                if v1[10] > 0 and v1[5] > 0:
                    v1[10] -= 1
                    v1[5] -= 1
                    v3 = True
                if not v3 and v1[5] >= 3:
                    v1[5] -= 3
                    v3 = True
                if not v3:
                    return False
        return True
