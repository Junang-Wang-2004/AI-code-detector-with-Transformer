class C1:

    def lengthOfLastWord(self, a1):
        v1 = len(a1) - 1
        while v1 >= 0 and a1[v1] == ' ':
            v1 -= 1
        v2 = 0
        while v1 >= 0 and a1[v1] != ' ':
            v2 += 1
            v1 -= 1
        return v2
