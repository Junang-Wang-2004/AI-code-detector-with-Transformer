class C1(object):

    def numberOfPowerfulInt(self, a1, a2, a3, a4):
        """
        """

        def count(a1):
            v1 = 0
            v2 = str(a1)
            v3 = len(v2) - len(a4)
            v4 = (a3 + 1) ** v3
            for v5 in range(v3):
                v4 //= a3 + 1
                v1 += (min(int(v2[v5]) - 1, a3) - 0 + 1) * v4
                if int(v2[v5]) > a3:
                    break
            else:
                if int(v2[-len(a4):]) >= int(a4):
                    v1 += 1
            return v1
        return count(a2) - count(a1 - 1)
