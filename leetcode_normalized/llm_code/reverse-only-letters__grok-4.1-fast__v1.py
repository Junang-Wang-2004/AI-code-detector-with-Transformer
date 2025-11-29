class C1:

    def reverseOnlyLetters(self, a1):
        v1 = list(a1)
        v2, v3 = (0, len(v1) - 1)
        while v2 < v3:
            while v2 < v3 and (not v1[v2].isalpha()):
                v2 += 1
            while v2 < v3 and (not v1[v3].isalpha()):
                v3 -= 1
            v1[v2], v1[v3] = (v1[v3], v1[v2])
            v2 += 1
            v3 -= 1
        return ''.join(v1)
