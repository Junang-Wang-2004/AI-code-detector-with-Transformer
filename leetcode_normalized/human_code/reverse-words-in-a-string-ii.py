class C1(object):

    def reverseWords(self, a1):
        """
        """

        def reverse(a1, a2, a3):
            for v1 in range((a3 - a2) / 2):
                a1[a2 + v1], a1[a3 - 1 - v1] = (a1[a3 - 1 - v1], a1[a2 + v1])
        reverse(a1, 0, len(a1))
        v1 = 0
        for v2 in range(len(a1) + 1):
            if v2 == len(a1) or a1[v2] == ' ':
                reverse(a1, v1, v2)
                v1 = v2 + 1
