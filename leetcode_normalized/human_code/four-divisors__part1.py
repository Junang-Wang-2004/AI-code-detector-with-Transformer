class C1(object):

    def sumFourDivisors(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            v3, v4 = ([], 1)
            while v4 * v4 <= v2:
                if v2 % v4:
                    v4 += 1
                    continue
                v3.append(v4)
                if v4 != v2 // v4:
                    v3.append(v2 // v4)
                    if len(v3) > 4:
                        break
                v4 += 1
            if len(v3) == 4:
                v1 += sum(v3)
        return v1
