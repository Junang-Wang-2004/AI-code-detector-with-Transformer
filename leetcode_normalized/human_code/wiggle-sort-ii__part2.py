from random import randint

class C1(object):

    def wiggleSort(self, a1):
        """
        """

        def nth_element(a1, a2, a3=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4, a5):
                v1 = a2
                while v1 <= a3:
                    if a1[v1] == a4:
                        v1 += 1
                    elif a5(a1[v1], a4):
                        a1[a2], a1[v1] = (a1[v1], a1[a2])
                        a2 += 1
                        v1 += 1
                    else:
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                return (a2, a3)
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = randint(v1, v2)
                v4, v5 = tri_partition(a1, v1, v2, a1[v3], a3)
                if v4 <= a2 <= v5:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v5 + 1

        def reversedTriPartitionWithVI(a1, a2):

            def idx(a1, a2):
                return (1 + 2 * a1) % a2
            v1 = len(a1) / 2 * 2 + 1
            v2, v3, v4 = (0, 0, len(a1) - 1)
            while v3 <= v4:
                if a1[idx(v3, v1)] > a2:
                    a1[idx(v2, v1)], a1[idx(v3, v1)] = (a1[idx(v3, v1)], a1[idx(v2, v1)])
                    v2 += 1
                    v3 += 1
                elif a1[idx(v3, v1)] < a2:
                    a1[idx(v3, v1)], a1[idx(v4, v1)] = (a1[idx(v4, v1)], a1[idx(v3, v1)])
                    v4 -= 1
                else:
                    v3 += 1
        v1 = (len(a1) - 1) // 2
        nth_element(a1, v1)
        reversedTriPartitionWithVI(a1, a1[v1])
