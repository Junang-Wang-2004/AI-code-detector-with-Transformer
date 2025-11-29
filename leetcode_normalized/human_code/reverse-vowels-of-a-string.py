class C1(object):

    def reverseVowels(self, a1):
        """
        """
        v1 = 'aeiou'
        v2 = list(a1)
        v3, v4 = (0, len(a1) - 1)
        while v3 < v4:
            if v2[v3].lower() not in v1:
                v3 += 1
            elif v2[v4].lower() not in v1:
                v4 -= 1
            else:
                v2[v3], v2[v4] = (v2[v4], v2[v3])
                v3 += 1
                v4 -= 1
        return ''.join(v2)
