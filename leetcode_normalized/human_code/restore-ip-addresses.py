class C1(object):

    def restoreIpAddresses(self, a1):
        v1 = []
        self.restoreIpAddressesRecur(v1, a1, 0, '', 0)
        return v1

    def restoreIpAddressesRecur(self, a1, a2, a3, a4, a5):
        if (4 - a5) * 3 < len(a2) - a3 or 4 - a5 > len(a2) - a3:
            return
        if a3 == len(a2) and a5 == 4:
            a1.append(a4[:-1])
        else:
            for v1 in range(a3, a3 + 3):
                if len(a2) > v1 and self.isValid(a2[a3:v1 + 1]):
                    a4 += a2[a3:v1 + 1] + '.'
                    self.restoreIpAddressesRecur(a1, a2, v1 + 1, a4, a5 + 1)
                    a4 = a4[:-(v1 - a3 + 2)]

    def isValid(self, a1):
        if len(a1) == 0 or (a1[0] == '0' and a1 != '0'):
            return False
        return int(a1) < 256
