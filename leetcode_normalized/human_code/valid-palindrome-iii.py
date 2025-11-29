class C1(object):

    def isValidPalindrome(self, a1, a2):
        """
        """
        if a1 == a1[::-1]:
            return True
        v1 = [[1] * len(a1) for v2 in range(2)]
        for v3 in reversed(range(len(a1))):
            for v4 in range(v3 + 1, len(a1)):
                if a1[v3] == a1[v4]:
                    v1[v3 % 2][v4] = 2 + v1[(v3 + 1) % 2][v4 - 1] if v3 + 1 <= v4 - 1 else 2
                else:
                    v1[v3 % 2][v4] = max(v1[(v3 + 1) % 2][v4], v1[v3 % 2][v4 - 1])
        return len(a1) <= a2 + v1[0][-1]
