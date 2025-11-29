class C1(object):

    def monotoneIncreasingDigits(self, a1):
        v1 = list(str(a1))
        v2 = len(v1)
        v3 = v2 - 1
        while v3 > 0:
            if int(v1[v3 - 1]) <= int(v1[v3]):
                v3 -= 1
            else:
                v1[v3 - 1] = str(int(v1[v3 - 1]) - 1)
                for v4 in range(v3, v2):
                    v1[v4] = '9'
                v3 -= 1
        return int(''.join(v1))
