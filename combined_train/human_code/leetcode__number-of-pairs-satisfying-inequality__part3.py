import itertools

class C1(object):

    def numberOfPairs(self, a1, a2, a3):
        """
        """

        def merge_sort(a1, a2, a3, a4):
            if a2 == a3:
                return
            v1 = a2 + (a3 - a2) // 2
            merge_sort(a1, a2, v1, a4)
            merge_sort(a1, v1 + 1, a3, a4)
            v2 = v1 + 1
            for v3 in range(a2, v1 + 1):
                while v2 < a3 + 1 and a1[v3] - a1[v2] > a3:
                    v2 += 1
                a4[0] += a3 - v2 + 1
            v4 = []
            v3, v2 = (a2, v1 + 1)
            while v3 < v1 + 1 or v2 < a3 + 1:
                if v2 >= a3 + 1 or (v3 < v1 + 1 and a1[v3] <= a1[v2]):
                    v4.append(a1[v3])
                    v3 += 1
                else:
                    v4.append(a1[v2])
                    v2 += 1
            a1[a2:a3 + 1] = v4
        v1 = [x - y for v2, v3 in zip(a1, a2)]
        v4 = [0]
        merge_sort(v1, 0, len(v1) - 1, v4)
        return v4[0]
