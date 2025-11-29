import random

class C1(object):

    def sortArray(self, a1):
        """
        """

        def nth_element(a1, a2, a3, a4, a5=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4):
                v1 = a2
                while v1 <= a3:
                    if a5(a1[v1], a4):
                        a1[v1], a1[a2] = (a1[a2], a1[v1])
                        a2 += 1
                        v1 += 1
                    elif a5(a4, a1[v1]):
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                    else:
                        v1 += 1
                return (a2, a3)
            while a2 <= a4:
                v1 = random.randint(a2, a4)
                v2, v3 = tri_partition(a1, a2, a4, a1[v1])
                if v2 <= a3 <= v3:
                    return
                elif v2 > a3:
                    a4 = v2 - 1
                else:
                    a2 = v3 + 1

        def quickSort(a1, a2, a3):
            if a1 > a2:
                return
            v1 = a1 + (a2 - a1) // 2
            nth_element(a3, a1, v1, a2)
            quickSort(a1, v1 - 1, a3)
            quickSort(v1 + 1, a2, a3)
        quickSort(0, len(a1) - 1, a1)
        return a1
