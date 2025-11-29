class C1(object):

    def countBinaryPalindromes(self, a1):
        """
        """
        v1 = list(map(int, bin(a1)[2:]))
        v2 = len(v1) // 2
        return (1 << v2) - 1 + (a1 >> v2) + int(v1[:len(v1) - v2] + v1[:v2][::-1] <= v1)
