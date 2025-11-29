class C1(object):

    def sortEvenOdd(self, a1):
        """
        """

        def partition(a1, a2):
            for v1 in range(len(a2)):
                v2 = v1
                while a2[v1] >= 0:
                    v2 = a1(v2)
                    a2[v1], a2[v2] = (a2[v2], ~a2[v1])
            for v1 in range(len(a2)):
                a2[v1] = ~a2[v1]
        partition(lambda i: i // 2 if i % 2 == 0 else (len(a1) + 1) // 2 + i // 2, a1)
        a1[:(len(a1) + 1) // 2], a1[(len(a1) + 1) // 2:] = (sorted(a1[:(len(a1) + 1) // 2]), sorted(a1[(len(a1) + 1) // 2:], reverse=True))
        partition(lambda i: 2 * i if i < (len(a1) + 1) // 2 else 1 + 2 * (i - (len(a1) + 1) // 2), a1)
        return a1
