class C1(object):

    def nextPalindrome(self, a1):
        v1 = list(a1)
        v2 = len(v1)
        v3 = v2 // 2
        v4 = v3 - 2
        while v4 >= 0 and v1[v4] >= v1[v4 + 1]:
            v4 -= 1
        if v4 < 0:
            return ''
        v5 = v3 - 1
        while v5 > v4 and v1[v5] <= v1[v4]:
            v5 -= 1
        v1[v4], v1[v5] = (v1[v5], v1[v4])
        v1[v4 + 1:v3] = v1[v4 + 1:v3][::-1]
        v6 = v1[:v3][::-1]
        if v2 % 2 == 0:
            v1[v3:] = v6
        else:
            v1[v3 + 1:] = v6
        return ''.join(v1)
