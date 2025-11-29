class C1(object):

    def numberOfPowerfulInt(self, a1, a2, a3, a4):
        """
        """

        def count(a1):

            def length(a1):
                v1 = 0
                while a1:
                    a1 //= 10
                    v1 += 1
                return v1
            v1 = 0
            v2 = length(a1)
            v3 = 10 ** v2
            v4 = v2 - len(a4)
            v5 = (a3 + 1) ** v4
            for v6 in range(v4):
                v3 //= 10
                v7 = a1 // v3 % 10
                v5 //= a3 + 1
                v1 += (min(v7 - 1, a3) - 0 + 1) * v5
                if v7 > a3:
                    break
            else:
                if a1 % v3 >= int(a4):
                    v1 += 1
            return v1
        return count(a2) - count(a1 - 1)
