class C1(object):

    def reverseWords(self, a1):
        """
        """

        def reverse(a1, a2, a3):
            for v1 in range((a3 - a2) // 2):
                a1[a2 + v1], a1[a3 - 1 - v1] = (a1[a3 - 1 - v1], a1[a2 + v1])
        a1, v2 = (list(a1), 0)
        for v3 in range(len(a1) + 1):
            if v3 == len(a1) or a1[v3] == ' ':
                reverse(a1, v2, v3)
                v2 = v3 + 1
        return ''.join(a1)
