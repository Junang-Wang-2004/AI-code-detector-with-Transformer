class C1(object):

    def findProductsOfElements(self, a1):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1 >> 1)
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def f(a1):

            def count1(a1):
                v1 = v2 = 0
                while 1 << v2 <= a1:
                    v3 = (1 << v2 + 1) - 1
                    v1 += ((a1 & ~v3) >> 1) + max((a1 & v3) - (1 << v2) + 1, 0)
                    v2 += 1
                return v1

            def count2(a1):
                v1 = v2 = 0
                while 1 << v2 <= a1:
                    v3 = (1 << v2 + 1) - 1
                    v1 += (((a1 & ~v3) >> 1) + max((a1 & v3) - (1 << v2) + 1, 0)) * v2
                    v2 += 1
                return v1
            v1 = binary_search(1, a1 - 1, lambda i: count1(i) >= a1)
            v2 = count2(v1 - 1)
            a1 -= count1(v1 - 1)
            v4 = 0
            while 1 << v4 <= v1:
                if v1 & 1 << v4:
                    v2 += v4
                    a1 -= 1
                    if a1 == 0:
                        break
                v4 += 1
            return v2
        return [pow(2, f(right + 1) - f(left), mod) for v1, v2, v3 in a1]
