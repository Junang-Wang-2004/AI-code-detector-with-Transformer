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

        def inplace_counting_sort(a1, a2, a3, a4=False):
            if a3 - a2 + 1 == 0:
                return
            v1 = [0] * (max((a1[i] for v2 in range(a2, a3 + 1))) + 1)
            for v2 in range(a2, a3 + 1):
                v1[a1[v2]] += 1
            for v2 in range(1, len(v1)):
                v1[v2] += v1[v2 - 1]
            for v2 in reversed(range(a2, a3 + 1)):
                while a1[v2] >= 0:
                    v1[a1[v2]] -= 1
                    v3 = a2 + v1[a1[v2]]
                    a1[v2], a1[v3] = (a1[v3], ~a1[v2])
            for v2 in range(a2, a3 + 1):
                a1[v2] = ~a1[v2]
            if a4:
                while a2 < a3:
                    a1[a2], a1[a3] = (a1[a3], a1[a2])
                    a2 += 1
                    a3 -= 1
        partition(lambda i: i // 2 if i % 2 == 0 else (len(a1) + 1) // 2 + i // 2, a1)
        inplace_counting_sort(a1, 0, (len(a1) + 1) // 2 - 1)
        inplace_counting_sort(a1, (len(a1) + 1) // 2, len(a1) - 1, True)
        partition(lambda i: 2 * i if i < (len(a1) + 1) // 2 else 1 + 2 * (i - (len(a1) + 1) // 2), a1)
        return a1
