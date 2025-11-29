class C1(object):

    def countOddLetters(self, a1):
        """
        """
        v1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        v2 = [0] * 26
        while a1:
            a1, v4 = divmod(a1, 10)
            for v5 in v1[v4]:
                v2[ord(v5) - ord('a')] += 1
        return sum((v % 2 for v6 in v2))
