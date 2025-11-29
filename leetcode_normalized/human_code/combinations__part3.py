class C1(object):

    def combine(self, a1, a2):
        """
        """

        def combineDFS(a1, a2, a3, a4, a5):
            if a4 == 0:
                a5.append(a3[:])
                return
            for v1 in range(a2, a1):
                a3.append(v1 + 1)
                combineDFS(a1, v1 + 1, a3, a4 - 1, a5)
                a3.pop()
        v1 = []
        combineDFS(a1, 0, [], a2, v1)
        return v1
